import axios from 'axios'

export const getAllUsuario = async () => {
  try {
    const { data } = await axios.get('http://localhost:8000/usuarios', {
      headers: {
        'Content-Type': 'application/json',
        'Access-Control-Allow-Origin': 'http://localhost:3000' // Change this to your React app URL
      }
    });
    return data;
  } catch (error) {
    console.error(error);
    throw new Error('Unable to fetch usuarios');
  }
}
