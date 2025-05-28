import React, { useEffect, useState } from "react";
import { View, Text, ScrollView, StyleSheet, Alert } from "react-native";
import { Card, Divider } from "react-native-paper";
import { MaterialCommunityIcons, MaterialIcons } from "@expo/vector-icons";
import FontAwesome5 from "@expo/vector-icons/FontAwesome5";
import { Device } from '@/interfaces/Device';
import { PartError } from '@/interfaces/PartError';
import api from "@/services/api";

export default function Monitoring() {
  const [devices, setDevices] = useState<Device[]>([]);
  const [loading, setLoading] = useState(true);
  const [partsErrors, setPartsErrors] = useState<PartError | null>(null);

  useEffect(() => {
    const fetchDevices = async () => {
      try {
        const response = await api.get("/devices/");
        setDevices(response.data);
        setLoading(false);
        Alert.alert("Sucesso", "Dados carregados com sucesso!");
      } catch (err) {
        setLoading(false);
        Alert.alert("Erro", "Falha ao carregar dados");
      }
    };

    const fetchPartsErrors = async () => {
      try{
        const response = await api.get("/production-parts/parts/descarte/total")
        setPartsErrors(response.data);
        setLoading(false);
      }catch (err) {
        setLoading(false);
        Alert.alert("Erro", "Falha ao carregar dados");
      }
    }

    fetchDevices();
    fetchPartsErrors();
  }, []);

  return (
    <ScrollView style={styles.container}>
      {/* Cards */}
      

      {/* Lista de Sensores */}
        <Card style={styles.listCard}>
          <View style={styles.sectionHeader}>
            <Text style={styles.sectionTitle}>Sensores</Text>
          </View>
          {devices.filter(device => device.description.toLowerCase().includes("sensor")).flatMap((device) =>
            device.states.map((state) => (
              <View key={`${device.id}-${state.id}`}>
                <View style={styles.listItem}>
                  <View style={styles.listItemContent}>
                    <Text style={styles.listItemName}>{device.description}</Text>
                    <Text style={styles.listItemDateTime}>
                      {new Date(state.timestamp).toLocaleString()}
                    </Text>
                  </View>
                  <Text
                    style={[
                      styles.listItemStatus,
                      state.state ? styles.statusActive : styles.statusInactive,
                    ]}
                  >
                    {state.state ? "Ativo" : "Inativo"}
                  </Text>
                </View>
                <Divider style={styles.divider} />
              </View>
            ))
          )}
        </Card>

        <Card style={styles.listCard}>
          <View style={styles.sectionHeader}>
            <Text style={styles.sectionTitle}>Saídas</Text>
          </View>
          {devices.filter(device => !device.description.toLowerCase().includes("sensor")).flatMap((device) =>
            device.states.map((state) => (
              <View key={`${device.id}-${state.id}`}>
                <View style={styles.listItem}>
                  <View style={styles.listItemContent}>
                    <Text style={styles.listItemName}>{device.description}</Text>
                    <Text style={styles.listItemDateTime}>
                      {new Date(state.timestamp).toLocaleString()}
                    </Text>
                  </View>
                  <Text
                    style={[
                      styles.listItemStatus,
                      state.state ? styles.statusActive : styles.statusInactive,
                    ]}
                  >
                    {state.state ? "Ativo" : "Inativo"}
                  </Text>
                </View>
                <Divider style={styles.divider} />
              </View>
            ))
          )}
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
