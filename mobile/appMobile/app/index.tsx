import React, { useState, useEffect, useRef } from 'react';
import { View, Text, TextInput, TouchableOpacity, StyleSheet, Animated, Alert } from 'react-native';
import { IconSymbol } from '@/components/ui/IconSymbol';
import { useRouter } from 'expo-router';

export default function LoginScreen() {
  // Estados para controlar qual tela mostrar
  const [showForgotPassword, setShowForgotPassword] = useState(false);
  
  const router = useRouter();
  // Estados do formulário de login
  const [activeTab, setActiveTab] = useState('login');
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [confirmPassword, setConfirmPassword] = useState('');
  const [name, setName] = useState('');
  const [emailError, setEmailError] = useState('');
  const [nameError, setNameError] = useState('');
  
  // Animações
  const slideAnim = useRef(new Animated.Value(300)).current;

  useEffect(() => {
    Animated.timing(slideAnim, {
      toValue: 0,
      duration: 300,
      useNativeDriver: true,
    }).start();
  }, [showForgotPassword]); // Executa quando alterna entre telas

  const handleNameChange = (text: string) => {
    const lettersOnly = text.replace(/[^a-zA-ZÀ-ÿ\s]/g, '');
    setName(lettersOnly);
    if (/\d/.test(text)) setNameError('Nome não pode conter números');
    else setNameError('');
  };

  const handleEmailChange = (text: string) => {
    setEmail(text);
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (text && !emailRegex.test(text)) setEmailError('Por favor, insira um e-mail válido');
    else setEmailError('');
  };

  const handleForgotPassword = () => {
    if (!email) {
      Alert.alert('Atenção', 'Por favor, insira seu e-mail');
      return;
    }
    if (emailError) return;
    
    Alert.alert('Sucesso', `Um e-mail de recuperação foi enviado para: ${email}`);
    setShowForgotPassword(false);
  };

  const handleRegister = () => {
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

    if (emailError || nameError) {
      return;
    }

    Alert.alert('Sucesso', 'Cadastro realizado com sucesso!');
    setName('');
    setEmail('');
    setPassword('');
    setConfirmPassword('');
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
    
    Alert.alert('Login', 'Login realizado com sucesso!')
  };

  const handleAction = () => {
    if (activeTab === 'login') {
      handleLogin();
      router.push('/dashboard');
    }
    else handleRegister();
  };

  // Renderiza a tela de esqueci a senha
  if (showForgotPassword) {
    return (
      <View style={styles.container}>
        <Animated.View style={[styles.modalView, { transform: [{ translateY: slideAnim }] }]}>
          <View style={styles.recycleContainer}>
            <IconSymbol name="recycle" size={40} color="white" />
          </View>
          
          <Text style={styles.title}>Recuperar senha</Text>
          <Text style={styles.subtitle}>Digite seu e-mail para receber as instruções</Text>

          <TextInput
            style={[styles.input, emailError && styles.inputError]}
            placeholder="Digite seu e-mail"
            keyboardType="email-address"
            value={email}
            onChangeText={handleEmailChange}
          />
          {emailError && <Text style={styles.errorText}>{emailError}</Text>}

          <TouchableOpacity style={styles.actionButton} onPress={handleForgotPassword}>
            <Text style={styles.buttonText}>Enviar instruções</Text>
          </TouchableOpacity>

          <TouchableOpacity onPress={() => setShowForgotPassword(false)}>
            <Text style={styles.backText}>Voltar para login</Text>
          </TouchableOpacity>
        </Animated.View>
      </View>
    );
  }

  // Renderiza a tela normal de login/cadastro
  return (
    <View style={styles.container}>
      <Animated.View style={[styles.modalView, { transform: [{ translateY: slideAnim }] }]}>
        <View style={styles.recycleContainer}>
          <IconSymbol name="recycle" size={40} color="white" />
        </View>
        
        <View style={styles.tabContainer}>
          <TouchableOpacity
            style={[styles.tabButton, activeTab === 'login' && styles.activeTab]}
            onPress={() => setActiveTab('login')}
          >
            <Text style={styles.tabText}>Login</Text>
          </TouchableOpacity>

          <TouchableOpacity
            style={[styles.tabButton, activeTab === 'cadastro' && styles.activeTab]}
            onPress={() => setActiveTab('cadastro')}
          >
            <Text style={styles.tabText}>Cadastro</Text>
          </TouchableOpacity>
        </View>

        {activeTab === 'cadastro' && (
          <>
            <TextInput
              style={[styles.input, nameError && styles.inputError]}
              placeholder="Nome completo"
              value={name}
              onChangeText={handleNameChange}
            />
            {nameError && <Text style={styles.errorText}>{nameError}</Text>}
          </>
        )}

        <TextInput
          style={[styles.input, emailError && styles.inputError]}
          placeholder="E-mail"
          keyboardType="email-address"
          value={email}
          onChangeText={handleEmailChange}
        />
        {emailError && <Text style={styles.errorText}>{emailError}</Text>}

        <TextInput
          style={styles.input}
          placeholder="Senha"
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
          </>
        )}

        <TouchableOpacity style={styles.actionButton} onPress={handleAction}>
          <Text style={styles.buttonText}>{activeTab === 'login' ? 'Entrar' : 'Cadastrar'}</Text>
        </TouchableOpacity>

        {activeTab === 'login' && (
          <TouchableOpacity onPress={() => setShowForgotPassword(true)}>
            <Text style={styles.linkText}>Esqueci minha senha</Text>
          </TouchableOpacity>
        )}
      </Animated.View>
    </View>
  );
}

// Estilos (adicione esses novos estilos)
const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#f0f0f5',
    justifyContent: 'center',
    alignItems: 'center',
    padding: 20,
  },
  modalView: {
    width: '100%',
    maxWidth: 320,
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
  recycleContainer: {
    width: 100,
    height: 50,
    backgroundColor: '#7FA653',
    borderRadius: 10,
    justifyContent: 'center',
    alignItems: 'center',
    marginBottom: 20,
  },
  title: {
    fontSize: 20,
    fontWeight: 'bold',
    color: '#4B8707',
    marginBottom: 10,
  },
  subtitle: {
    fontSize: 14,
    color: '#555',
    textAlign: 'center',
    marginBottom: 20,
  },
  tabContainer: {
    flexDirection: 'row',
    backgroundColor: '#63783D',
    borderRadius: 30,
    padding: 5,
    marginBottom: 20,
  },
  tabButton: {
    flex: 1,
    paddingVertical: 10,
    alignItems: 'center',
    borderRadius: 8,
  },
  activeTab: {
    backgroundColor: '#7FA653',
    borderRadius: 30,
  },
  tabText: {
    color: 'white',
    fontSize: 16,
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
    color: 'white',
    fontSize: 18,
  },
  linkText: {
    marginTop: 15,
    color: '#4B8707',
    fontSize: 14,
  },
  backText: {
    marginTop: 15,
    color: '#4B8707',
    fontSize: 14,
  },
});