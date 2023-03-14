import axios from 'axios'
import { UsuarioModel } from '../model/UsuarioModel';


// Read by Id --Start

export const readByIdUsuario = async (id: number) => {
     return axios.create({ headers: { 'Content-Type': 'application/json' }})
     .get(`http://localhost:8000/usuario/${id}`);
 
 }
 // Read by Id --End
 
 // Read All --Start
 
 export const getAllUsuario = async () => {
 
     const { data } = await axios
     .create({ headers: { 'Content-Type': 'application/json' }})
     .get('http://localhost:8000/usuario');
 
     return data;
 
 }
 // Read All --End
 
 // Delete --Start
 
 export const deleteAirport = async (id: number) => {
 
     const UsuarioService = await axios
    .create({ headers: { 'Content-Type': 'application/json' }})
    .delete(`http://localhost:8000/usuario/${id}`);
 
     return UsuarioService;
 
 }
 // Delete --End
 
 // Create --Start
 
 export const createAirport = async ( data: UsuarioModel) => {
 
     const UsuarioService = await axios
   .create({ headers: { 'Content-Type': 'application/json' }})
   .post(`http://localhost:8000/usuario`, data);
 
     return UsuarioService;
 
 }
 // Create --End
 
 // Update --Start
 
 export const updateAirport = async (id: number, data: UsuarioModel) => {
 
     const UsuarioService = await axios
  .create({ headers: { 'Content-Type': 'application/json' }})
  .put(`http://localhost:8000/usuario/${id}`, data);
 
     return UsuarioService;
 
 }
 // Update --End