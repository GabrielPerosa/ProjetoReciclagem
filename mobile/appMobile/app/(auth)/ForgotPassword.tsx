import React, { useState, useRef, useEffect } from 'react';
import { View, Text, TextInput, TouchableOpacity, StyleSheet, Animated, Alert } from 'react-native';
import { IconSymbol } from '@/components/ui/IconSymbol';
import { useNavigation } from '@react-navigation/native';

export default function ForgotPasswordScreen() {
  const [email, setEmail] = useState('');
  const [emailError, setEmailError] = useState('');
  const slideAnim = useRef(new Animated.Value(300)).current;
  const navigation = useNavigation();

  useEffect(() => {
    Animated.timing(slideAnim, {
      toValue: 0,
      duration: 300,
      useNativeDriver: true,
    }).start();
  }, []);

  const handleEmailChange = (text: string) => {
    setEmail(text);
    
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (text && !emailRegex.test(text)) {
      setEmailError('Por favor, insira um e-mail válido');
    } else {
      setEmailError('');
    }
  };

  const handleRecoverPassword = () => {
    if (!email) {
      Alert.alert('Atenção', 'Por favor, insira seu e-mail');
      return;
    }
    
    if (emailError) {
      return;
    }
    
    Alert.alert('Sucesso', `Um e-mail de recuperação foi enviado para: ${email}`);
    navigation.goBack();
  };

  return (
    <View style={styles.container}>
      <Animated.View style={[styles.content, { transform: [{ translateY: slideAnim }] }]}>
        <View style={styles.recycleContainer}>
          <IconSymbol 
            name="recycle"
            size={40}
            color="white"
            style={{ marginBottom: 10, marginTop: 10 }}
          />
        </View>
        
        <Text style={styles.title}>Recuperar senha</Text>
        <Text style={styles.subtitle}>Digite seu e-mail para receber as instruções de recuperação</Text>

        <TextInput
          style={[styles.input, emailError ? styles.inputError : null]}
          placeholder="Digite seu e-mail"
          keyboardType="email-address"
          autoCapitalize="none"
          value={email}
          onChangeText={handleEmailChange}
        />
        {emailError ? <Text style={styles.errorText}>{emailError}</Text> : null}

        <TouchableOpacity 
          style={styles.actionButton}
          onPress={handleRecoverPassword}
        >
          <Text style={styles.buttonText}>Enviar instruções</Text>
        </TouchableOpacity>

        <TouchableOpacity onPress={() => navigation.goBack()}>
          <Text style={styles.backText}>Voltar para login</Text>
        </TouchableOpacity>
      </Animated.View>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#f0f0f5',
    justifyContent: 'center',
    alignItems: 'center',
    padding: 20,
  },
  content: {
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
    marginBottom: 10,
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
  backText: {
    marginTop: 15,
    fontSize: 14,
    color: '#4B8707',
  },
});