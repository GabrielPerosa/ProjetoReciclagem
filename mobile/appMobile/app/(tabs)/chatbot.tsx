import React, { useEffect, useRef, useState } from 'react';
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
import api from '@/services/api';
import { Message } from "@/interfaces/Message";

export default function Chatbot() {
  const [messages, setMessages] = useState<Message[]>([]);
  const [input, setInput] = useState('');
  const scrollViewRef = useRef<ScrollView>(null);

  const sendMessage = async () => {
    if (!input.trim()) return; // evita enviar mensagens vazias

    const userMessage: Message = { sender: 'user', text: input };
    setMessages(prev => [...prev, userMessage]); // adiciona a mensagem do usuário imediatamente
    setInput(''); // limpa o campo de entrada

    try {
      const response = await api.post("/chat/prompt", {
        message: input
      });

      // adiciona a resposta do chatbot ao estado, concatenando com mensagens anteriores
      setMessages(prev => [...prev, { sender: 'bot', text: response.data.response }]);
    } catch (err) {
      console.error("Erro ao enviar mensagem:", err);
    }
  };

  // Auto-scroll para a última mensagem ao atualizar messages
  useEffect(() => {
    scrollViewRef.current?.scrollToEnd({ animated: true });
  }, [messages]);

  return (
    <KeyboardAvoidingView
      style={styles.container}
      behavior={Platform.OS === 'ios' ? "padding" : undefined}
      keyboardVerticalOffset={Platform.OS === 'ios' ? 60 : 0} // Ajuste do offset para iOS
    >
      <View style={styles.modalView}>
        <Text style={styles.title}>Chatbot</Text>
        <ScrollView
          ref={scrollViewRef}
          style={styles.messagesContainer}
          contentContainerStyle={{ paddingVertical: 10 }}
          keyboardShouldPersistTaps="handled"
        >
          {messages.map((msg, index) => (
            <View
              key={index} // melhor gerar um id único em produção
              style={msg.sender === 'user' ? styles.userMessage : styles.botMessage}
            >
              <Text style={msg.sender === 'user' ? styles.userText : styles.botText}>{msg.text}</Text>
            </View>
          ))}
        </ScrollView>
        <View style={styles.inputRow}>
          <TextInput
            style={styles.input}
            value={input}
            onChangeText={setInput}
            placeholder="Digite sua mensagem..."
            placeholderTextColor="#555"
            onSubmitEditing={sendMessage} // permite enviar com Enter no teclado
            returnKeyType="send"
          />
          <TouchableOpacity style={styles.actionButton} onPress={sendMessage}>
            <MaterialIcons name="send" size={24} color="white" />
          </TouchableOpacity>
        </View>
      </View>
    </KeyboardAvoidingView>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#f0f0f5',
    padding: 40,
    justifyContent: 'center',
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
  inputRow: {
    flexDirection: 'row',
    alignItems: 'center',
  },
  input: {
    flex: 1,
    height: 50,
    borderWidth: 1,
    borderColor: '#4B8707',
    borderRadius: 8,
    paddingHorizontal: 10,
    color: '#000',
  },
  actionButton: {
    width: 50,
    height: 50,
    backgroundColor: '#7FA653',
    borderRadius: 25,
    justifyContent: 'center',
    alignItems: 'center',
    marginLeft: 10,
  },
});
