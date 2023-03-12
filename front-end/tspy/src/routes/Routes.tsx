import { Routes, Route, Navigate } from 'react-router-dom'
import { Home } from '../pages/home/Home'
import { Login } from '../pages/login/Login'


export const AppRoutes = () => {

    return(
        <Routes>
            <Route path='/home' element={<Home/>}/> 
            <Route path='/login' element={<Login />}/> 
            
            <Route path='*' element={<Navigate to='/home' />} />
        </Routes>
    )

}