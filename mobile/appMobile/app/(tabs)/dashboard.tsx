import React from 'react';
import { View, Text, ScrollView, Dimensions, StyleSheet } from 'react-native';
import { LineChart } from 'react-native-chart-kit';
import { Card } from 'react-native-paper';
import MaterialCommunityIcons from '@expo/vector-icons/MaterialCommunityIcons';
import FontAwesome5 from '@expo/vector-icons/FontAwesome5';


export default function Dashboard() {
    const data = {
        labels: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'],
        datasets: [
            {
                data: [10, 20, 15, 30, 25, 40],
                strokeWidth: 2,
            },
        ],
    };

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
                    <Text style={[styles.percentageText, styles.percentageDay]}>100%</Text>
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
                    <Text style={[styles.percentageText, styles.percentageMonth]}>93%</Text>
                </View>
            </Card>

            {/* Card - Gráfico de Performance */}
            <Card style={styles.chartContainer}>
                <View style={styles.cardHeader}>
                    <View style={styles.iconContainer}>
                        <MaterialCommunityIcons name="chart-line" size={24} color="#fff" />
                    </View>
                    <View style={styles.headerContent}>
                        <Text style={styles.cardTitle}>Performance</Text>
                    </View>
                </View>
                <View style={styles.cardContent}>
                    <LineChart
                        data={data}
                        width={Dimensions.get('window').width - 40}
                        height={220}
                        chartConfig={{
                            backgroundColor: '#ffffff',
                            backgroundGradientFrom: '#ffffff',
                            backgroundGradientTo: '#ffffff',
                            decimalPlaces: 0,
                            color: (opacity = 1) => `rgba(0, 0, 255, ${opacity})`,
                            labelColor: (opacity = 1) => `rgba(0, 0, 0, ${opacity})`,
                        }}
                        bezier
                        style={{ marginVertical: 8 }}
                    />
                </View>
            </Card>
        </ScrollView>
    );
}

const styles = StyleSheet.create({
    container: {
      flex: 1,
      backgroundColor: '#f5f5f5',
    },
    scrollContent: {
      padding: 20,
      paddingTop: 50,
    },
    card: {
      marginBottom: 20,
      overflow: 'hidden',
      backgroundColor: '#fff',
      borderRadius: 8,
      elevation: 3,
    },
    cardHeader: {
      backgroundColor: '#7AA46B',
      padding: 15,
      flexDirection: 'row',
      alignItems: 'center',
      justifyContent: 'center',
      position: 'relative',
    },
    headerContent: {
      flexDirection: 'row',
      alignItems: 'center',
      justifyContent: 'center',
      width: '100%',
    },
    cardTitle: {
      fontWeight: 'bold',
      fontSize: 16,
      textAlign: 'center',
      marginLeft: 30, // Compensa o espaço do ícone
      color: "#fff"
    },
    iconContainer: {
      position: 'absolute',
      left: 15,
    },
    cardContent: {
      padding: 15,
    },
    row: {
      flexDirection: 'row',
      justifyContent: 'space-between',
      marginBottom: 10,
    },
    column: {
      alignItems: 'center',
      flex: 1,
    },
    boldText: {
      fontWeight: 'bold',
      marginBottom: 5,
      fontSize: 16,
    },
    labelText: {
      fontSize: 14,
      color: '#555',
    },
    percentageText: {
      fontSize: 24,
      fontWeight: 'bold',
      textAlign: 'center',
      marginVertical: 10,
    },
    percentageDay: {
      color: '#2ecc71',
    },
    percentageMonth: {
      color: '#f39c12',
    },
    chartContainer: {
      padding: 0,
      overflow: 'hidden',
      marginBottom: 30,
    },
  });
  