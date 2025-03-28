import React from 'react';
import { View, Text, ScrollView, Dimensions } from 'react-native';
import { LineChart } from 'react-native-chart-kit';
import { Card, Avatar } from 'react-native-paper';

export default function Dashboard() {
    const data = {
        labels: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'],
        datasets: [
            {
                data: [5, 15, 10, 25, 20, 35],
                strokeWidth: 2,
            },
        ],
    };

    return (
        <ScrollView style={{ padding: 20, backgroundColor: '#f5f5f5' }}>
            <Text style={{ fontSize: 24, fontWeight: 'bold', marginBottom: 20 }}>Dashboard</Text>
            
            <Card style={{ marginBottom: 20, padding: 15 }}>
                <Card.Title title="User Status" left={(props) => <Avatar.Icon {...props} icon="account-circle" />} />
                <Text style={{ fontSize: 18, color: 'blue', textAlign: 'center' }}>Active Users: 120</Text>
            </Card>

            <Card style={{ padding: 15 }}>
                <Card.Title title="Traffic Overview" left={(props) => <Avatar.Icon {...props} icon="chart-bar" />} />
                <LineChart
                    data={data}
                    width={Dimensions.get('window').width - 40}
                    height={220}
                    chartConfig={{
                        backgroundColor: '#ffffff',
                        backgroundGradientFrom: '#ffffff',
                        backgroundGradientTo: '#ffffff',
                        decimalPlaces: 0,
                        color: (opacity = 1) => `rgba(255, 99, 132, ${opacity})`,
                        labelColor: (opacity = 1) => `rgba(0, 0, 0, ${opacity})`,
                    }}
                    bezier
                    style={{ marginVertical: 8 }}
                />
            </Card>
        </ScrollView>
    );
}
