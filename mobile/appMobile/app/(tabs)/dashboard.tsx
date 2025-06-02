import React, { useState, useRef, useEffect } from "react";
import {View, Text, ScrollView, Dimensions, StyleSheet, Animated, Easing, TouchableOpacity} from "react-native";
import { LineChart } from "react-native-chart-kit";
import { Card, Avatar } from "react-native-paper";
import api from "@/services/api";
import { format } from "date-fns";
import { useAuth } from "@/services/AuthContext";
import { useRouter } from "expo-router";
import { MaterialIcons, FontAwesome5, MaterialCommunityIcons} from "@expo/vector-icons";

export default function Dashboard() {
  // Animações para scroll e progresso diário/mensal
  const scrollX = useRef(new Animated.Value(0)).current;
  const dayProgressAnim = useRef(new Animated.Value(0)).current;
  const monthProgressAnim = useRef(new Animated.Value(0)).current;

  // Estados para controle de porcentagens de aproveitamento no dia e no mês
  const [dayPercentage, setDayPercentage] = useState(0);
  const [monthPercentage, setMonthPercentage] = useState(0);

  // Indica qual gráfico está ativo (ex: 0 = diário, 1 = mensal)
  const [activeChart, setActiveChart] = useState(0);

  // Autenticação e roteamento
  const { logout, token, loading } = useAuth();
  const router = useRouter();

  // Largura da tela do dispositivo
  const screenWidth = Dimensions.get("window").width;

  // Dados totais do dia e do mês para os 3 tipos de materiais
  const [dayData, setDayData] = useState({
    metalicas: 0,
    plasticas: 0,
    descarte: 0,
  });
  const [monthData, setMonthData] = useState({
    metalicas: 0,
    plasticas: 0,
    descarte: 0,
  });

  // Rótulos dos meses usados no gráfico mensal
  const monthLabels = ["Jan", "Fev", "Mar", "Abr", "Mai", "Jun", "Jul", "Ago", "Set", "Out", "Nov", "Dez"];

  // Estado com os dados do gráfico mensal (um dataset para cada tipo de material)
  const [monthlyChartData, setMonthlyChartData] = useState({
    labels: monthLabels,
    datasets: [
      {
        data: Array(12).fill(0),
        color: () => "rgba(0,0,255,1)",
        strokeWidth: 2,
      }, // metalicas
      {
        data: Array(12).fill(0),
        color: () => "rgba(255,165,0,1)",
        strokeWidth: 2,
      }, // plasticas
      {
        data: Array(12).fill(0),
        color: () => "rgba(255,0,0,1)",
        strokeWidth: 2,
      }, // descarte
    ],
  });

  // Redireciona o usuário para a tela de login caso não esteja autenticado
  useEffect(() => {
    if (!loading) {
      if (!token) {
        router.replace("/"); // Redireciona para login
      }
    }
  }, [loading, token]);

  // Anima as barras de progresso de forma suave sempre que as porcentagens mudam
  useEffect(() => {
    Animated.parallel([
      Animated.timing(dayProgressAnim, {
        toValue: dayPercentage, // Progresso diário
        duration: 3000,
        easing: Easing.out(Easing.quad),
        useNativeDriver: false,
      }),
      Animated.timing(monthProgressAnim, {
        toValue: monthPercentage, // Progresso mensal
        duration: 3000,
        easing: Easing.out(Easing.quad),
        useNativeDriver: false,
      }),
    ]).start();
  }, [dayPercentage, monthPercentage]);

  // Busca e processa os dados da API quando o componente é carregado
  useEffect(() => {
    const fetchData = async () => {
      const res = await api.get("/production-parts/summary"); // Chamada à API
      const data = res.data;

      const today = format(new Date(), "dd/MM/yyyy"); // Data atual
      const currentMonth = format(new Date(), "MM/yyyy"); // Mês atual

      const materials = ["metalicas", "plasticas", "descarte"] as const;

      // Inicializa os totais do dia e do mês
      let todayTotals = { metalicas: 0, plasticas: 0, descarte: 0 };
      let monthTotals = { metalicas: 0, plasticas: 0, descarte: 0 };

      // Para cada tipo de material, soma os valores do dia e do mês atual
      materials.forEach((type) => {
        const entries = data[type] || {};
        for (const dateKey in entries) {
          const hourData = entries[dateKey];
          const totalOnDate = Object.values(hourData).reduce(
            (sum: number, qty: any) => sum + Number(qty),
            0
          );

          // Soma total do dia
          if (dateKey === today) {
            todayTotals[type] += totalOnDate;
          }

          // Verifica se é do mês atual
          const [d, m, y] = dateKey.split("/");
          if (`${m}/${y}` === currentMonth) {
            monthTotals[type] += totalOnDate;
          }
        }
      });

      // Atualiza estados com os totais
      setDayData(todayTotals);
      setMonthData(monthTotals);

      // Calcula a porcentagem de aproveitamento (sem considerar descartes)
      const totalDay =
        todayTotals.metalicas + todayTotals.plasticas + todayTotals.descarte;
      const totalMonth =
        monthTotals.metalicas + monthTotals.plasticas + monthTotals.descarte;

      setDayPercentage(
        totalDay > 0
          ? ((todayTotals.metalicas + todayTotals.plasticas) / totalDay) * 100
          : 0
      );

      setMonthPercentage(
        totalMonth > 0
          ? ((monthTotals.metalicas + monthTotals.plasticas) / totalMonth) * 100
          : 0
      );

      // --- Agrega os dados por mês para o gráfico ---
      const monthlyBuckets = {
        metalicas: Array(12).fill(0),
        plasticas: Array(12).fill(0),
        descarte: Array(12).fill(0),
      };

      // Agrupa os totais de cada material por mês
      materials.forEach((type) => { // Percorre cada tipo de material: 'metalicas', 'plasticas' e 'descarte'
        const entries = data[type] || {}; // Obtém os registros do tipo atual. Se não existir, usa objeto vazio
        for (const dateKey in entries) { // Para cada data registrada nesse tipo de material
          const [day, month, year] = dateKey.split("/"); // Divide a data (formato dd/MM/yyyy) em dia, mês e ano
          const dt = new Date(Number(year), Number(month) - 1, Number(day)); // Cria um objeto Date com o ano, mês (ajustado para base 0) e dia
          const monthIndex = dt.getMonth(); // Pega o índice do mês (de 0 a 11), usado para mapear nos arrays mensais
          const dayTotal = Object.values(entries[dateKey]).reduce( // Soma todas as quantidades daquele dia (em diferentes horários, por exemplo)
            (sum: number, qty: any) => sum + Number(qty),// Converte cada valor para número e acumula
            0
          );
          monthlyBuckets[type][monthIndex] += dayTotal; // Adiciona esse total no mês correspondente dentro do array daquele material
        } 
      });

      // Atualiza os dados do gráfico com os totais mensais agrupados
      setMonthlyChartData({
        labels: monthLabels,
        datasets: [
          { ...monthlyChartData.datasets[0], data: monthlyBuckets.metalicas },
          { ...monthlyChartData.datasets[1], data: monthlyBuckets.plasticas },
          { ...monthlyChartData.datasets[2], data: monthlyBuckets.descarte },
        ],
      });
    };

    fetchData(); // Executa a função ao montar o componente
  }, []);

  const charts = [
    {
      id: 1,
      title: "Contador de Peças (Mensal)",
      icon: "chart-line",
      component: (
        <View style={styles.chartContainer}>
          <LineChart
            data={monthlyChartData}
            width={screenWidth * 0.9}
            height={220}
            chartConfig={{
              backgroundColor: "#ffffff",
              backgroundGradientFrom: "#ffffff",
              backgroundGradientTo: "#ffffff",
              decimalPlaces: 0,
              color: (opacity = 1) => `rgba(0, 0, 0, ${opacity})`,
              labelColor: (opacity = 1) => `rgba(0, 0, 0, ${opacity})`,
              propsForLabels: { fontSize: 12 },
            }}
            bezier
            style={{ marginVertical: 8, borderRadius: 16 }}
            fromZero
          />
          <View style={styles.legendContainer}>
            <View style={styles.legendItem}>
              <View
                style={[styles.legendColor, { backgroundColor: "#0000FF" }]}
              />
              <Text style={styles.legendText}>Metalicas</Text>
            </View>
            <View style={styles.legendItem}>
              <View
                style={[styles.legendColor, { backgroundColor: "#FFA500" }]}
              />
              <Text style={styles.legendText}>Plasticas</Text>
            </View>
            <View style={styles.legendItem}>
              <View
                style={[styles.legendColor, { backgroundColor: "#FF0000" }]}
              />
              <Text style={styles.legendText}>Descartes</Text>
            </View>
          </View>
        </View>
      ),
    },
  ];

  return (
    <ScrollView
      style={styles.container}
      contentContainerStyle={styles.scrollContent}
      showsVerticalScrollIndicator={false}
    >
      <TouchableOpacity onPress={logout} style={styles.logout}>
        <MaterialIcons name="logout" size={24} color="green" />
        <Text style={styles.Textlogout}>Logout</Text>
      </TouchableOpacity>

      {/* Card - Dados do Dia */}
      <Card style={styles.card}>
        <View style={styles.cardHeader}>
          <View style={styles.iconContainer}>
            <MaterialCommunityIcons name="cylinder" size={24} color="#fff" />
          </View>
          <View style={styles.headerContent}>
            <Text style={styles.cardTitle}>Dados do Dia</Text>
          </View>
        </View>
        <View style={styles.cardContent}>
          <View style={styles.row}>
            <View style={styles.column}>
              <Text style={styles.boldText}>{dayData.metalicas}</Text>
              <Text style={styles.labelText}>Metalicas</Text>
            </View>
            <View style={styles.column}>
              <Text style={styles.boldText}>{dayData.plasticas}</Text>
              <Text style={styles.labelText}>Plasticas</Text>
            </View>
            <View style={styles.column}>
              <Text style={styles.boldText}>{dayData.descarte}</Text>
              <Text style={styles.labelText}>Descartes</Text>
            </View>
            <View style={styles.column}>
              <Text style={styles.boldText}>
                {dayData.metalicas + dayData.plasticas + dayData.descarte}
              </Text>
              <Text style={styles.labelText}>Total</Text>
            </View>
          </View>
        </View>
      </Card>

      {/* Card - Aproveitamento do Dia */}
      <Card style={styles.card}>
        <View style={styles.cardHeader}>
          <View style={styles.iconContainer}>
            <FontAwesome5 name="percentage" size={24} color="#fff" />
          </View>
          <View style={styles.headerContent}>
            <Text style={styles.cardTitle}>Aproveitamento do Dia</Text>
          </View>
        </View>
        <View style={styles.cardContent}>
          <View style={styles.progressWrapper}>
            <Text style={[styles.percentageText, styles.percentageDay]}>
              {dayPercentage.toFixed(0)}%
            </Text>
            <View style={styles.progressContainer}>
              <View style={styles.progressBackground}>
                <Animated.View
                  style={[
                    styles.progressFill,
                    {
                      width: dayProgressAnim.interpolate({
                        inputRange: [0, 100],
                        outputRange: ["0%", "100%"],
                      }),
                      backgroundColor: "#2ecc71",
                    },
                  ]}
                />
              </View>
            </View>
          </View>
        </View>
      </Card>

      {/* Card - Dados por Mês */}
      <Card style={styles.card}>
        <View style={styles.cardHeader}>
          <View style={styles.iconContainer}>
            <MaterialCommunityIcons name="cylinder" size={24} color="#fff" />
          </View>
          <View style={styles.headerContent}>
            <Text style={styles.cardTitle}>Dados por Mês</Text>
          </View>
        </View>
        <View style={styles.cardContent}>
          <View style={styles.row}>
            <View style={styles.column}>
              <Text style={styles.boldText}>{monthData.metalicas}</Text>
              <Text style={styles.labelText}>Metalicas</Text>
            </View>
            <View style={styles.column}>
              <Text style={styles.boldText}>{monthData.plasticas}</Text>
              <Text style={styles.labelText}>Plasticas</Text>
            </View>
            <View style={styles.column}>
              <Text style={styles.boldText}>{monthData.descarte}</Text>
              <Text style={styles.labelText}>Descartes</Text>
            </View>
            <View style={styles.column}>
              <Text style={styles.boldText}>
                {monthData.metalicas + monthData.plasticas + monthData.descarte}
              </Text>
              <Text style={styles.labelText}>Total</Text>
            </View>
          </View>
        </View>
      </Card>

      {/* Card - Aproveitamento do Mês */}
      <Card style={styles.card}>
        <View style={styles.cardHeader}>
          <View style={styles.iconContainer}>
            <FontAwesome5 name="percentage" size={24} color="#fff" />
          </View>
          <View style={styles.headerContent}>
            <Text style={styles.cardTitle}>Aproveitamento do Mês</Text>
          </View>
        </View>
        <View style={styles.cardContent}>
          <View style={styles.progressWrapper}>
            <Text style={[styles.percentageText, styles.percentageMonth]}>
              {monthPercentage.toFixed(0)}%
            </Text>
            <View style={styles.progressContainer}>
              <View style={styles.progressBackground}>
                <Animated.View
                  style={[
                    styles.progressFill,
                    {
                      width: monthProgressAnim.interpolate({
                        inputRange: [0, 100],
                        outputRange: ["0%", "100%"],
                      }),
                      backgroundColor: "#f39c12",
                    },
                  ]}
                />
              </View>
            </View>
          </View>
        </View>
      </Card>

      {/* Container de gráficos */}
      <View>
        <ScrollView
          showsHorizontalScrollIndicator={false}
          onScroll={Animated.event(
            [{ nativeEvent: { contentOffset: { x: scrollX } } }],
            { useNativeDriver: false }
          )}
          onMomentumScrollEnd={(e) =>
            setActiveChart(
              Math.round(e.nativeEvent.contentOffset.x / screenWidth)
            )
          }
        >
          {charts.map((chart) => (
            <View key={chart.id}>
              <Card style={styles.chartCard}>
                <Card.Title
                  title={chart.title}
                  left={(props) => <Avatar.Icon {...props} icon={chart.icon} />}
                  titleStyle={styles.chartTitle}
                />
                <View style={styles.chartContent}>{chart.component}</View>
              </Card>
            </View>
          ))}
        </ScrollView>
      </View>
    </ScrollView>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: "#f5f5f5",
  },
  scrollContent: {
    padding: 10,
    paddingTop: 90,
  },
  logout: {
    position: "absolute",
    top: 40,
    right: 9,
    zIndex: 1,
    backgroundColor: "#f5f5f5",
    padding: 10,
    borderRadius: 50,
    flexDirection: "row",
  },
  Textlogout: {
    fontSize: 12,
    color: "green",
    marginLeft: 5,
    fontWeight: "bold",
    marginTop: 5,
  },
  card: {
    marginBottom: 20,
    overflow: "hidden",
    backgroundColor: "#fff",
    borderRadius: 8,
    elevation: 3,
  },
  cardHeader: {
    backgroundColor: "#7AA46B",
    padding: 15,
    flexDirection: "row",
    alignItems: "center",
    justifyContent: "center",
    position: "relative",
  },
  headerContent: {
    flexDirection: "row",
    alignItems: "center",
    justifyContent: "center",
    width: "100%",
  },
  cardTitle: {
    fontWeight: "bold",
    fontSize: 16,
    textAlign: "center",
    marginLeft: 30,
    color: "#fff",
  },
  iconContainer: {
    position: "absolute",
    left: 15,
  },
  cardContent: {
    padding: 15,
  },
  row: {
    flexDirection: "row",
    justifyContent: "space-between",
    marginBottom: 10,
  },
  column: {
    alignItems: "center",
    flex: 1,
  },
  boldText: {
    fontWeight: "bold",
    marginBottom: 5,
    fontSize: 16,
  },
  labelText: {
    fontSize: 14,
    color: "#555",
  },
  percentageText: {
    fontSize: 24,
    fontWeight: "bold",
    minWidth: 60,
  },
  percentageDay: {
    color: "#2ecc71",
  },
  percentageMonth: {
    color: "#f39c12",
  },

  chartCard: {
    overflow: "hidden",
    backgroundColor: "#fff",
    borderRadius: 12,
    width: "100%",
  },
  chartTitle: {
    fontWeight: "bold",
    color: "#333",
  },
  chartContainer: {
    alignItems: "center",
    justifyContent: "center",
  },
  chartContent: {
    paddingHorizontal: 5,
    paddingBottom: 15,
  },
  legendContainer: {
    flexDirection: "row",
    justifyContent: "center",
    marginTop: 10,
    flexWrap: "wrap",
  },
  legendItem: {
    flexDirection: "row",
    alignItems: "center",
    marginHorizontal: 10,
    marginVertical: 5,
  },
  legendColor: {
    width: 12,
    height: 12,
    borderRadius: 6,
    marginRight: 5,
  },
  legendText: {
    fontSize: 12,
    color: "#555",
  },
  progressWrapper: {
    flexDirection: "row",
    alignItems: "center",
    justifyContent: "space-between",
    paddingHorizontal: 10,
  },
  progressContainer: {
    flex: 1,
    marginLeft: 15,
  },
  progressBackground: {
    height: 10,
    backgroundColor: "#e0e0e0",
    borderRadius: 5,
    overflow: "hidden",
  },
  progressFill: {
    height: "100%",
    borderRadius: 5,
  },
});
