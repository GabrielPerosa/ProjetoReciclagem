import React, { useState, useEffect, useRef } from 'react';
import { View, Text, TextInput, TouchableOpacity, StyleSheet, Modal, Animated, Alert } from 'react-native';
import { IconSymbol } from '@/components/ui/IconSymbol';

export default function LoginScreen() {
  const [visible, setVisible] = useState(true);
  const [activeTab, setActiveTab] = useState('login');
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [confirmPassword, setConfirmPassword] = useState('');
  const [name, setName] = useState('');
  const [acceptTerms, setAcceptTerms] = useState(false);
  const [emailError, setEmailError] = useState('');
  const [nameError, setNameError] = useState('');
  const slideAnim = useRef(new Animated.Value(300)).current;

  useEffect(() => {
    if (visible) {
      Animated.timing(slideAnim, {
        toValue: 0,
        duration: 300,
        useNativeDriver: true,
      }).start();
    }
  }, [visible]);

  // Validação do nome (não aceita números)
  const handleNameChange = (text: string) => {
    const lettersOnly = text.replace(/[^a-zA-ZÀ-ÿ\s]/g, '');
    setName(lettersOnly);
    
    if (/\d/.test(text)) {
      setNameError('Nome não pode conter números');
    } else {
      setNameError('');
    }
  };

  // Validação do e-mail
  const handleEmailChange = (text: string) => {
    setEmail(text);
    
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (text && !emailRegex.test(text)) {
      setEmailError('Por favor, insira um e-mail válido');
    } else {
      setEmailError('');
    }
  };

  const handleRegister = () => {
    // Validações adicionais antes de cadastrar
    if (!name) {
      setNameError('Por favor, insira seu nome completo');
      return;
    }
    
    if (!email) {
      setEmailError('Por favor, insira seu e-mail');
      return;
    }
    
    if (!password || !confirmPassword) {
      Alert.alert('Atenção', 'Por favor, preencha todos os campos obrigatórios');
      return;
    }

    if (password !== confirmPassword) {
      Alert.alert('Atenção', 'As senhas não coincidem');
      return;
    }

    if (!acceptTerms) {
      Alert.alert('Atenção', 'Você deve aceitar os termos de uso');
      return;
    }

    if (emailError || nameError) {
      return; // Não prossegue se houver erros de validação
    }

    Alert.alert('Sucesso', 'Cadastro realizado com sucesso!');
    setName('');
    setEmail('');
    setPassword('');
    setConfirmPassword('');
    setAcceptTerms(false);
    setActiveTab('login');
  };

  const handleLogin = () => {
    if (!email || !password) {
      Alert.alert('Atenção', 'Por favor, preencha todos os campos');
      return;
    }
    
    if (emailError) {
      return;
    }
    
    Alert.alert('Login', 'Login realizado com sucesso!');
  };

  const handleAction = () => {
    if (activeTab === 'login') {
      handleLogin();
    } else {
      handleRegister();
    }
  };

  return (
    <View style={styles.container}>
      <Modal animationType="fade" transparent visible={visible}>
        <View style={styles.overlay} />
        <View style={styles.centeredView}>
          <Animated.View style={[styles.modalView, { transform: [{ translateY: slideAnim }] }]}>
            <View style={styles.recycleContainer}>
              <IconSymbol 
                name="recycle"
                size={30}
                color="white"
                style={{ marginBottom: 10 }}
              />
            </View>
            
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

            {activeTab === 'cadastro' && (
              <>
                <TextInput
                  style={[styles.input, nameError ? styles.inputError : null]}
                  placeholder="Nome completo"
                  value={name}
                  onChangeText={handleNameChange}
                />
                {nameError ? <Text style={styles.errorText}>{nameError}</Text> : null}
              </>
            )}

            <TextInput
              style={[styles.input, emailError ? styles.inputError : null]}
              placeholder="Digite seu e-mail"
              keyboardType="email-address"
              autoCapitalize="none"
              value={email}
              onChangeText={handleEmailChange}
            />
            {emailError ? <Text style={styles.errorText}>{emailError}</Text> : null}

            <TextInput
              style={styles.input}
              placeholder="Digite sua senha"
              secureTextEntry
              value={password}
              onChangeText={setPassword}
            />

            {activeTab === 'cadastro' && (
              <>
                <TextInput
                  style={styles.input}
                  placeholder="Confirme sua senha"
                  secureTextEntry
                  value={confirmPassword}
                  onChangeText={setConfirmPassword}
                />
                
                <View style={styles.termsContainer}>
                  <TouchableOpacity
                    style={[styles.checkbox, acceptTerms && styles.checkboxChecked]}
                    onPress={() => setAcceptTerms(!acceptTerms)}
                  >
                    {acceptTerms && <Text style={styles.checkIcon}>✓</Text>}
                  </TouchableOpacity>
                  <Text style={styles.termsText}>
                    Concordo com os termos de uso
                  </Text>
                </View>
              </>
            )}

            <TouchableOpacity 
              style={styles.actionButton}
              onPress={handleAction}
            >
              <Text style={styles.buttonText}>{activeTab === 'login' ? 'Entrar' : 'Cadastrar'}</Text>
            </TouchableOpacity>

            <TouchableOpacity onPress={() => setVisible(false)}>
              <Text style={styles.closeText}>Esqueci minha senha</Text>
            </TouchableOpacity>
          </Animated.View>
        </View>
      </Modal>
    </View>
  );
}

// Estilos (adicionando os novos estilos necessários)
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
    elevation: 5,
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
    backgroundColor: '#4CAF50',
    borderRadius: 10,
    justifyContent: 'center',
    alignItems: 'center',
    marginBottom: 10,
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
  inputError: {
    borderColor: '#FF0000',
  },
  errorText: {
    color: '#FF0000',
    fontSize: 12,
    alignSelf: 'flex-start',
    marginBottom: 5,
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
  termsContainer: {
    flexDirection: 'row',
    alignItems: 'center',
    marginVertical: 10,
    alignSelf: 'flex-start',
  },
  checkbox: {
    width: 20,
    height: 20,
    borderWidth: 1,
    borderColor: '#4B8707',
    borderRadius: 4,
    marginRight: 10,
    justifyContent: 'center',
    alignItems: 'center',
  },
  checkboxChecked: {
    backgroundColor: '#4B8707',
  },
  checkIcon: {
    color: 'white',
    fontSize: 12,
  },
  termsText: {
    fontSize: 14,
    color: '#555',
  },
});