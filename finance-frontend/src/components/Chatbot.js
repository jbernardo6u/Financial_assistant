import React, { useState } from 'react';
import axios from 'axios';

function Chatbot() {
  const [message, setMessage] = useState('');
  const [response, setResponse] = useState('');

  const handleSendMessage = () => {
    axios.post('http://localhost:8000/api/chatbot/', { message })
      .then(res => setResponse(res.data.message))
      .catch(error => setResponse("Erreur lors de l'interaction avec le chatbot."));
  };

  return (
    <div>
      <h1>Chatbot</h1>
      <textarea
        placeholder="Posez votre question"
        value={message}
        onChange={(e) => setMessage(e.target.value)}
      />
      <button onClick={handleSendMessage}>Envoyer</button>
      {response && <p>Réponse du Chatbot: {response}</p>}
    </div>
  );
}

export default Chatbot;
