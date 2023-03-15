

import axios from "axios"
import { useEffect, useState } from "react";
/* import { Usuario } from "../model/Usuario"; */
import {  getAllUsuario } from "../../services/Usuarios"

export function Usuarios() {
  const [ usuarios, setUsuarios ] = useState<any[]>();

  const loadData = async () => {
    const usuarios: any[] = await getAllUsuario();
    setUsuarios(usuarios);
  }

  useEffect(() => {
    loadData();
  }, []);

  return (
    <div>
      <table>
        <thead>
          <td>Código</td>
          <td>Nome</td>
          <td>Sobrenome</td>
          <td>Ações</td>
        </thead>
        <tbody>
          {
            usuarios?.map(usuario => {
              return (
                <tr>
                  <td>{usuario.nome}</td>
                  <td>{usuario.email}</td>
                  <td>{usuario.senha}</td>
                </tr>
              )
            })
          }
        </tbody>
      </table>
    </div>
  )
}