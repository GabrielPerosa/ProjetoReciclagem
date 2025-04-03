import React, { useState, useRef, useEffect } from "react";
import {
  View,
  Text,
  ScrollView,
  Dimensions,
  StyleSheet,
  Animated,
  Easing,
} from "react-native";
import { LineChart } from "react-native-chart-kit";
import { Card, Avatar } from "react-native-paper";
import MaterialCommunityIcons from "@expo/vector-icons/MaterialCommunityIcons";
import FontAwesome5 from "@expo/vector-icons/FontAwesome5";

export default function Dashboard() {
  const scrollX = useRef(new Animated.Value(0)).current;
  const dayProgressAnim = useRef(new Animated.Value(0)).current;
  const monthProgressAnim = useRef(new Animated.Value(0)).current;
  const [activeChart, setActiveChart] = useState(0);
  const screenWidth = Dimensions.get("window").width;

  useEffect(() => {
    Animated.parallel([
      Animated.timing(dayProgressAnim, {
        toValue: 100,
        duration: 3000,
        easing: Easing.out(Easing.quad),
        useNativeDriver: false,
      }),
      Animated.timing(monthProgressAnim, {
        toValue: 93,
        duration: 3000,
        easing: Easing.out(Easing.quad),
        useNativeDriver: false,
      })
    ]).start();
  }, []);

  const charts = [
    {
      id: 1,
      title: "Contador de peças nas rampas",
      icon: "chart-line",
      component: (
        <View style={styles.chartContainer}>
          <LineChart
            data={{
              labels: ["Seg", "Ter", "Qua", "Qui", "Sex", "Sab"],
              datasets: [
                {
                  data: [16, 14, 12, 10, 8, 6],
                  color: (opacity = 1) => `rgba(0, 100, 0, ${opacity})`,
                  strokeWidth: 3,
                },
                {
                  data: [14, 12, 10, 8, 6, 4],
                  color: (opacity = 1) => `rgba(0, 0, 255, ${opacity})`,
                  strokeWidth: 3,
                },
                {
                  data: [2, 1, 0, 1, 2, 0],
                  color: (opacity = 1) => `rgba(255, 0, 0, ${opacity})`,
                  strokeWidth: 3,
                },
              ],
            }}
            width={screenWidth * 0.9}
            height={220}
            chartConfig={{
              backgroundColor: "#ffffff",
              backgroundGradientFrom: "#ffffff",
              backgroundGradientTo: "#ffffff",
              decimalPlaces: 0,
              color: (opacity = 1) => `rgba(0, 0, 0, ${opacity})`,
              labelColor: (opacity = 1) => `rgba(0, 0, 0, ${opacity})`,
              style: {
                borderRadius: 16,
              },
              propsForLabels: {
                fontSize: 12,
              },
              propsForDots: {
                r: "4",
                strokeWidth: "2",
                stroke: "#ffffff",
              },
            }}
            bezier
            style={{
              marginVertical: 8,
              borderRadius: 16,
            }}
            fromZero
          />
          <View style={styles.legendContainer}>
            <View style={styles.legendItem}>
              <View style={[styles.legendColor, { backgroundColor: "#006400" }]} />
              <Text style={styles.legendText}>Rampa 01</Text>
            </View>
            <View style={styles.legendItem}>
              <View style={[styles.legendColor, { backgroundColor: "#0000FF" }]} />
              <Text style={styles.legendText}>Rampa 02</Text>
            </View>
            <View style={styles.legendItem}>
              <View style={[styles.legendColor, { backgroundColor: "#FF0000" }]} />
              <Text style={styles.legendText}>Rejeitados</Text>
            </View>
          </View>
        </View>
      ),
    },
    {
      id: 2,
      title: "Contador de peças",
      icon: "chart-line",
      component: (
        <View style={styles.chartContainer}>
          <LineChart
            data={{
              labels: ["Jan", "Fev", "Mar", "Abr", "Mai", "Jun", "Jul", "Ago", "Set", "Out", "Nov", "Dez"],
              datasets: [
                {
                  data: [120, 140, 160, 180, 200, 220, 200, 180, 200, 220, 240, 260],
                  color: (opacity = 1) => `rgba(0, 0, 255, ${opacity})`,
                  strokeWidth: 2,
                },
                {
                  data: [80, 100, 120, 140, 160, 180, 160, 140, 160, 180, 200, 220],
                  color: (opacity = 1) => `rgba(255, 165, 0, ${opacity})`,
                  strokeWidth: 2,
                },
                {
                  data: [10, 12, 8, 15, 20, 18, 15, 12, 10, 8, 5, 3],
                  color: (opacity = 1) => `rgba(255, 0, 0, ${opacity})`,
                  strokeWidth: 2,
                },
              ],
            }}
            width={screenWidth * 0.9}
            height={220}
            chartConfig={{
              backgroundColor: "#ffffff",
              backgroundGradientFrom: "#ffffff",
              backgroundGradientTo: "#ffffff",
              decimalPlaces: 0,
              color: (opacity = 1) => `rgba(0, 0, 0, ${opacity})`,
              labelColor: (opacity = 1) => `rgba(0, 0, 0, ${opacity})`,
              propsForLabels: {
                fontSize: 12,
              },
            }}
            bezier
            style={{
              marginVertical: 8,
              borderRadius: 16,
            }}
            fromZero
          />
          <View style={styles.legendContainer}>
            <View style={styles.legendItem}>
              <View style={[styles.legendColor, { backgroundColor: "#0000FF" }]} />
              <Text style={styles.legendText}>Metal</Text>
            </View>
            <View style={styles.legendItem}>
              <View style={[styles.legendColor, { backgroundColor: "#FFA500" }]} />
              <Text style={styles.legendText}>Plástico</Text>
            </View>
            <View style={styles.legendItem}>
              <View style={[styles.legendColor, { backgroundColor: "#FF0000" }]} />
              <Text style={styles.legendText}>Rejeitados</Text>
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
              <Text style={styles.boldText}>06</Text>
              <Text style={styles.labelText}>Rampa 01</Text>
            </View>
            <View style={styles.column}>
              <Text style={styles.boldText}>04</Text>
              <Text style={styles.labelText}>Rampa 02</Text>
            </View>
            <View style={styles.column}>
              <Text style={styles.boldText}>0</Text>
              <Text style={styles.labelText}>Refugo</Text>
            </View>
            <View style={styles.column}>
              <Text style={styles.boldText}>12</Text>
              <Text style={styles.labelText}>Peças</Text>
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
            <Text style={[styles.percentageText, styles.percentageDay]}>100%</Text>
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
              <Text style={styles.boldText}>100</Text>
              <Text style={styles.labelText}>Rampa 01</Text>
            </View>
            <View style={styles.column}>
              <Text style={styles.boldText}>200</Text>
              <Text style={styles.labelText}>Rampa 02</Text>
            </View>
            <View style={styles.column}>
              <Text style={styles.boldText}>20</Text>
              <Text style={styles.labelText}>Refugo</Text>
            </View>
            <View style={styles.column}>
              <Text style={styles.boldText}>320</Text>
              <Text style={styles.labelText}>Peças</Text>
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
            <Text style={[styles.percentageText, styles.percentageMonth]}>93%</Text>
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
      <View style={styles.chartsSection}>
        <View style={styles.chartIndicatorContainer}>
          {charts.map((_, i) => (
            <View
              key={i}
              style={[
                styles.chartIndicator,
                activeChart === i && styles.activeChartIndicator,
              ]}
            />
          ))}
        </View>
        <ScrollView
          horizontal
          pagingEnabled
          showsHorizontalScrollIndicator={false}
          onScroll={Animated.event(
            [{ nativeEvent: { contentOffset: { x: scrollX } } }],
            { useNativeDriver: false }
          )}
          onMomentumScrollEnd={(e) => {
            const index = Math.round(e.nativeEvent.contentOffset.x / screenWidth);
            setActiveChart(index);
          }}
          style={styles.chartsScrollView}
        >
          {charts.map((chart) => (
            <View key={chart.id} style={[styles.chartWrapper, { width: screenWidth }]}>
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
    paddingTop: 50,
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
  chartsSection: {
    marginBottom: 30,
  },
  chartIndicatorContainer: {
    flexDirection: "row",
    justifyContent: "center",
    marginBottom: 10,
  },
  chartIndicator: {
    width: 8,
    height: 8,
    borderRadius: 4,
    backgroundColor: "#ccc",
    marginHorizontal: 4,
  },
  activeChartIndicator: {
    backgroundColor: "#7AA46B",
  },
  chartsScrollView: {
    marginHorizontal: -20,
  },
  chartWrapper: {
    paddingHorizontal: 20,
  },
  chartCard: {
    overflow: "hidden",
    backgroundColor: "#fff",
    borderRadius: 12,
    elevation: 3,
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