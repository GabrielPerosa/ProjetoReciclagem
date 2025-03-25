import React, { useState, useEffect, useRef } from 'react';
import { View, Text, TextInput, TouchableOpacity, StyleSheet, Modal, Animated } from 'react-native';
import { IconSymbol } from '@/components/ui/IconSymbol';

export default function LoginScreen() {
  const [visible, setVisible] = useState(true);
  const [activeTab, setActiveTab] = useState('login'); // Alterna entre login/cadastro
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [confirmPassword, setConfirmPassword] = useState('');
  const slideAnim = useRef(new Animated.Value(300)).current; // Inicia fora da tela

  // Animação ao abrir o modal
  useEffect(() => {
    if (visible) {
      Animated.timing(slideAnim, {
        toValue: 0,
        duration: 300,
        useNativeDriver: true,
      }).start();
    }
  }, [visible]);

  return (
    <View style={styles.container}>
      <Modal animationType="fade" transparent visible={visible}>
        <View style={styles.overlay} />
        <View style={styles.centeredView}>
          <Animated.View style={[styles.modalView, { transform: [{ translateY: slideAnim }] }]}>
            <View style={styles.recycleContainer}>
              <IconSymbol 
                name="recycle"
                size={30}  // Tamanho do ícone
                color="white"  // Cor do ícone
                style={{ marginBottom: 10 }}  // Estilo adicional, se necessário
              />
          </View>
            {/* Botões Login / Cadastro */}
            <View style={styles.tabContainer}>
              <TouchableOpacity
                style={[styles.tabButton, activeTab === 'login' && styles.activeTab]}
                onPress={() => setActiveTab('login')}
              >
                <Text style={[styles.tabText, activeTab === 'login' && styles.activeText]}>Login</Text>
              </TouchableOpacity>

              <TouchableOpacity
                style={[styles.tabButton, activeTab === 'cadastro' && styles.activeTab]}
                onPress={() => setActiveTab('cadastro')}
              >
                <Text style={[styles.tabText, activeTab === 'cadastro' && styles.activeText]}>Cadastro</Text>
              </TouchableOpacity>
            </View>

            {/* Campos de Entrada */}
            <TextInput
              style={styles.input}
              placeholder="Digite seu e-mail"
              keyboardType="email-address"
              autoCapitalize="none"
              value={email}
              onChangeText={setEmail}
            />

            <TextInput
              style={styles.input}
              placeholder="Digite sua senha"
              secureTextEntry
              value={password}
              onChangeText={setPassword}
            />

            {activeTab === 'cadastro' && (
              <TextInput
                style={styles.input}
                placeholder="Confirme sua senha"
                secureTextEntry
                value={confirmPassword}
                onChangeText={setConfirmPassword}
              />
            )}

            {/* Botão de ação */}
            <TouchableOpacity style={styles.actionButton}>
              <Text style={styles.buttonText}>{activeTab === 'login' ? 'Entrar' : 'Cadastrar'}</Text>
            </TouchableOpacity>

            {/* Fechar Modal */}
            <TouchableOpacity onPress={() => setVisible(false)}>
              <Text style={styles.closeText}>Esqueci minha senha</Text>
            </TouchableOpacity>
          </Animated.View>
        </View>
      </Modal>
    </View>
  );
}

// Estilos
const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#f0f0f5',
    justifyContent: 'center',
    alignItems: 'center',
  },
  overlay: {
    position: 'absolute',
    width: '100%',
    height: '100%',
    backgroundColor: 'rgba(0, 0, 0, 0.5)',
  },
  centeredView: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
  },
  modalView: {
    width: 320,
    backgroundColor: 'white',
    borderRadius: 15,
    padding: 20,
    alignItems: 'center',
    elevation: 5, // Sombra para Android
    shadowColor: '#000',
    shadowOffset: { width: 0, height: 2 },
    shadowOpacity: 0.25,
    shadowRadius: 4,
  },
  tabContainer: {
    flexDirection: 'row',
    backgroundColor: '#63783D',
    borderRadius: 30,
    padding: 5,
    marginBottom: 20,
  },
  recycleContainer: {
    width: 50,
    height: 50,
    backgroundColor: '#4CAF50', // Verde
    borderRadius: 10,
    justifyContent: 'center',
    alignItems: 'center',
    marginBottom: 10, // Espaço entre o ícone e os botões
  },
  tabButton: {
    flex: 1,
    paddingVertical: 10,
    alignItems: 'center',
    borderRadius: 8,
  },
  activeTab: {
    borderRadius: 30,
    backgroundColor: '#7FA653',
  },
  tabText: {
    fontSize: 16,
    color: '#fff',
  },
  activeText: {
    color: '#fff',
    fontWeight: 'bold',
  },
  input: {
    width: '100%',
    height: 50,
    borderWidth: 1,
    borderColor: '#4B8707',
    borderRadius: 8,
    paddingHorizontal: 10,
    marginBottom: 10,
  },
  actionButton: {
    width: '100%',
    height: 50,
    backgroundColor: '#7FA653',
    justifyContent: 'center',
    alignItems: 'center',
    borderRadius: 8,
    marginTop: 10,
  },
  buttonText: {
    color: '#fff',
    fontSize: 18,
  },
  closeText: {
    marginTop: 10,
    fontSize: 14,
    color: '#4B8707',
  },
});