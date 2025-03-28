import React from "react";
import { View, Text, ScrollView, StyleSheet } from "react-native";
import { Card, Divider } from "react-native-paper";
import { MaterialCommunityIcons, MaterialIcons } from "@expo/vector-icons";
import FontAwesome5 from '@expo/vector-icons/FontAwesome5';

export default function Monitoring() {
  // Dados para os sensores
  const sensors = [
    {
      name: "Óptico - Rampa 1",
      datatime: "25/03/2025 - 11:30",
      status: "Ativado",
    },
    {
      name: "Óptico - Rampa 2",
      datatime: "25/03/2025 - 11:30",
      status: "Desativado",
    },
    {
      name: "Óptico - Esteira",
      datatime: "25/03/2025 - 11:30",
      status: "Desativado",
    },
    {
      name: "Óptico - Altura peças",
      datatime: "25/03/2025 - 11:30",
      status: "Desativado",
    },
    {
      name: "Sensor Induitivo",
      datatime: "25/03/2025 - 11:30",
      status: "Ativado",
    },
    {
      name: "Sensor Capacitivo",
      datatime: "25/03/2025 - 11:30",
      status: "Desativado",
    },
  ];

  const exits = [
    { name: "Atuador 1", datatime: "25/03/2025 - 11:30", status: "Avançado" },
    { name: "Atuador 2", datatime: "25/03/2025 - 11:30", status: "Recuado" },
    { name: "Esteira", datatime: "25/03/2025 - 11:30", status: "Ligada" },
  ];

  return (
    <ScrollView style={styles.container}>
      {/* Cards*/}
      <View style={styles.cardsContainer}>
        <Card style={styles.mobileCard}>
          <View style={styles.cardContent}>
            <MaterialCommunityIcons name="clock" size={24} color="#4CAF50" />
            <View style={styles.cardTextContainer}>
              <Text style={styles.cardValue}>20 min</Text>
              <Text style={styles.cardLabel}>Tempo de Processo</Text>
            </View>
          </View>
        </Card>

        <Card style={styles.mobileCard}>
          <View style={styles.cardContent}>
            <MaterialIcons name="pause-circle-filled" size={24} color="#FF9800" />
            <View style={styles.cardTextContainer}>
              <Text style={styles.cardValue}>20 min</Text>
              <Text style={styles.cardLabel}>Última Parada</Text>
            </View>
          </View>
        </Card>

        <Card style={styles.mobileCard}>
          <View style={styles.cardContent}>
          <FontAwesome5 name="exclamation-triangle" size={18} color="red" />
            <View style={styles.cardTextContainer}>
              <Text style={styles.cardValue}>30</Text>
              <Text style={styles.cardLabel}>Erros</Text>
            </View>
          </View>
        </Card>
      </View>

      {/* Lista de Sensores */}
      <Card style={styles.listCard}>
        <View style={styles.sectionHeader}>
          <Text style={styles.sectionTitle}>Sensores</Text>
        </View>
        <Card.Content>
          {sensors.map((sensor, index) => (
            <View key={index}>
              <View style={styles.listItem}>
                <View style={styles.listItemContent}>
                  <Text style={styles.listItemName}>{sensor.name}</Text>
                  <Text style={styles.listItemDateTime}>{sensor.datatime}</Text>
                </View>
                <Text
                  style={[
                    styles.listItemStatus,
                    sensor.status === "Ativado" 
                      ? styles.statusActive 
                      : styles.statusInactive
                  ]}
                >
                  {sensor.status}
                </Text>
              </View>
              {index < sensors.length - 1 && <Divider style={styles.divider} />}
            </View>
          ))}
        </Card.Content>
      </Card>

      {/* Lista de Saídas */}
      <Card style={styles.listCard}>
        <View style={styles.sectionHeader}>
          <Text style={styles.sectionTitle}>Saídas</Text>
        </View>
        <Card.Content>
          {exits.map((exit, index) => (
            <View key={index}>
              <View style={styles.listItem}>
                <View style={styles.listItemContent}>
                  <Text style={styles.listItemName}>{exit.name}</Text>
                  <Text style={styles.listItemDateTime}>{exit.datatime}</Text>
                </View>
                <Text
                  style={[
                    styles.listItemStatus,
                    (exit.status === "Avançado" || exit.status === "Ligada") 
                      ? styles.statusActive 
                      : styles.statusInactive
                  ]}
                >
                  {exit.status}
                </Text>
              </View>
              {index < exits.length - 1 && <Divider style={styles.divider} />}
            </View>
          ))}
        </Card.Content>
      </Card>
    </ScrollView>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    padding: 10,
    backgroundColor: "#f5f5f5",
  },
  cardsContainer: {
    marginBottom: 15,
    marginTop: 20,
  },
  mobileCard: {
    backgroundColor: "#fff",
    elevation: 2,
    borderRadius: 8,
    padding: 15,
    marginTop: 20,
  },
  cardContent: {
    flexDirection: "row",
    alignItems: "center",
  },
  cardTextContainer: {
    marginLeft: 15,
  },
  cardValue: {
    fontSize: 18,
    fontWeight: "bold",
    color: "#2c3e50",
  },
  cardLabel: {
    fontSize: 14,
    color: "#7f8c8d",
    marginTop: 2,
  },
  listCard: {
    marginBottom: 20,
    backgroundColor: "#fff",
    elevation: 2,
    borderRadius: 8,
  },
  sectionHeader: {
    backgroundColor: "#7AA46B",
    paddingVertical: 12,
    borderTopLeftRadius: 8,
    borderTopRightRadius: 8,
  },
  sectionTitle: {
    fontSize: 18,
    fontWeight: "bold",
    color: "#fff",
    textAlign: "center",
  },
  listItem: {
    flexDirection: "row",
    justifyContent: "space-between",
    alignItems: "center",
    paddingVertical: 12,
    paddingHorizontal: 8,
  },
  listItemContent: {
    flex: 1,
  },
  listItemName: {
    fontSize: 14,
    fontWeight: "500",
    color: "#333",
    marginBottom: 4,
  },
  listItemDateTime: {
    fontSize: 12,
    color: "#666",
  },
  listItemStatus: {
    fontSize: 14,
    fontWeight: "bold",
    paddingHorizontal: 10,
    paddingVertical: 4,
    borderRadius: 12,
    minWidth: 90,
    textAlign: "center",
  },
  statusActive: {
    backgroundColor: "rgba(39, 174, 96, 0.1)",
    color: "#27ae60",
  },
  statusInactive: {
    backgroundColor: "rgba(231, 76, 60, 0.1)",
    color: "#e74c3c",
  },
  divider: {
    marginVertical: 0,
    backgroundColor: "#eee",
  },
});