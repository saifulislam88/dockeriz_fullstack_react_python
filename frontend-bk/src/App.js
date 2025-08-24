import React, { useState } from 'react';
import axios from 'axios';

function App() {
  const [form, setForm] = useState({ name: '', email: '', batch: '' });
  const handleChange = (e) => setForm({ ...form, [e.target.name]: e.target.value });
  const handleSubmit = async () => {
    await axios.post('/api/submit', form);
    alert('Submitted!');
  };
  return (
    <div>
      <input name="name" onChange={handleChange} placeholder="Name" />
      <input name="email" onChange={handleChange} placeholder="Email" />
      <input name="batch" onChange={handleChange} placeholder="Batch" />
      <button onClick={handleSubmit}>Submit</button>
    </div>
  );
}

export default App;
