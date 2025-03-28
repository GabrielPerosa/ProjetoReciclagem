import React, { useState } from 'react';
import {
  View,
  Text,
  TextInput,
  TouchableOpacity,
  StyleSheet,
  ScrollView,
  KeyboardAvoidingView,
  Platform
} from 'react-native';
import MaterialIcons from '@expo/vector-icons/MaterialIcons';

export default function Chatbot() {
  const [messages, setMessages] = useState([]);
  const [input, setInput] = useState('');

  const sendMessage = () => {
    if (input.trim() !== '') {
      setMessages(prev => [
        ...prev,
        { id: Date.now(), text: input, sender: 'user' }
      ]);
      setInput('');
    }
  };

  return (
    <KeyboardAvoidingView
      style={styles.container}
      behavior={Platform.OS === 'ios' ? "padding" : undefined}
    >
      <View style={styles.modalView}>
        <Text style={styles.title}>Chatbot</Text>
        <ScrollView 
          style={styles.messagesContainer}
          contentContainerStyle={{ paddingVertical: 10 }}
        >
          {messages.map(msg => (
            <View
              key={msg.id}
              style={msg.sender === 'user' ? styles.userMessage : styles.botMessage}
            >
              <Text style={msg.sender === 'user' ? styles.userText : styles.botText}>{msg.text}</Text>
            </View>
          ))}
        </ScrollView>
        <View style={styles.inputContainer}>
          <TextInput
            style={styles.input}
            value={input}
            onChangeText={setInput}
            placeholder="Digite sua mensagem..."
            placeholderTextColor="#555"
          />
        </View>
        <TouchableOpacity style={styles.actionButton} onPress={sendMessage}>
            <MaterialIcons name="send" size={24} color="white" /> {/* Usando o ícone de envio do MaterialIcons */}
        </TouchableOpacity>
      </View>
    </KeyboardAvoidingView>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#f0f0f5',
    padding: 20,
    justifyContent: 'center', // Centraliza verticalmente o conteúdo
    alignItems: 'center',
  },
  modalView: {
    flex: 1,
    width: '100%',
    maxWidth: 320,
    backgroundColor: 'white',
    borderRadius: 15,
    marginTop: 30,
    padding: 20,
    elevation: 5,
    shadowColor: '#000',
    shadowOffset: { width: 0, height: 2 },
    shadowOpacity: 0.25,
    shadowRadius: 4,
  },
  title: {
    fontSize: 20,
    fontWeight: 'bold',
    color: '#4B8707',
    marginBottom: 10,
  },
  messagesContainer: {
    flex: 1,
    width: '100%',
    marginBottom: 10,
  },
  userMessage: {
    alignSelf: 'flex-end',
    backgroundColor: '#7FA653',
    borderRadius: 10,
    padding: 10,
    marginBottom: 5,
    maxWidth: '80%',
  },
  botMessage: {
    alignSelf: 'flex-start',
    backgroundColor: '#e5e5e5',
    borderRadius: 10,
    padding: 10,
    marginBottom: 5,
    maxWidth: '80%',
  },
  userText: {
    color: 'white',
  },
  botText: {
    color: 'black',
  },
  inputContainer: {
    flexDirection: 'column',
    width: '100%',
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
    width: 40, // Tamanho do botão
    height: 40, // Tamanho do botão
    backgroundColor: '#7FA653',
    borderRadius: 30, // Tornando o botão redondo
    justifyContent: 'center',
    alignItems: 'center',
    marginBottom: 15,
    position: 'absolute', // Usando absolute para posicionar em relação ao container
    right: 25, // Distância da borda direita
    bottom: 20,
  },
  buttonText: {
    color: 'white',
    fontSize: 30, // Tamanho do texto do botão
  },
});