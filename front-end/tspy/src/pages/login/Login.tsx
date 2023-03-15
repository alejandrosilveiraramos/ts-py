
import React from 'react'

import { Paper, Container, CssBaseline, Grid, ListItem,  Typography, TextField, Link, Divider, Button } from '@mui/material'
import Checkbox from '@mui/material/Checkbox';

export const Login = () => {


    return (
        <React.Fragment>
            
            <CssBaseline />
            <Container sx={{ display: 'flex', justifyContent: 'center', width: '100vw', paddingTop: '3rem'  }} maxWidth="xl">
                <Paper sx={{ height: 'auto', width: '350px', padding: '3rem 2rem', display: 'flex', alignItems: 'center', justifyContent: 'center'}}>
                    <Grid container sx={{display: 'flex', alignItems: 'center', flexDirection: 'column', marginTop: '1rem'}}>
                        <Grid container sx={{display: 'flex', alignItems: 'center', flexDirection: 'column', marginTop: '1rem'}}>
                            <Grid>
                            <Typography sx={{fontSize: '1.55rem', textAlign: 'center', marginBottom: '1rem'}} fontWeight='bold' >Login</Typography>
                            </Grid>
                            <Grid item sx={{ width: '100%', margin: '.5rem 0'}} >
                            <TextField
                                id="outlined-password-input"
                                size='medium'
                                label="E-mail"
                                type="email"
                                autoComplete="current-email"
                                sx={{ width: '100%'}}
                                />
                            </Grid>
                            <Grid  item sx={{ width: '100%', margin: '.5rem 0'}}>
                            <TextField
                                id="outlined-password-input"
                                size='medium'
                                label="Password"
                                type="password"
                                autoComplete="current-password"
                                sx={{ width: '100%' }}
                                />
                                
                            </Grid>
                            <Grid item sx={{ width: '100%'}}>
                                <ListItem sx={{display: 'flex', justifyContent: 'space-between', alignItems: 'center', paddingLeft: '0', paddingRight: '0'}}>
                                    <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'center'}}>
                                    <Checkbox defaultChecked size="medium"   />
                                    <Typography>Mantenha me conectado</Typography>
                                    </div>
                                    <Link sx={{fontSize: '1.2rem'}}>Esqueceu a senha ?</Link>
                                </ListItem>
                                <ListItem sx={{display: 'flex', flexDirection: 'column', alignItems: 'center', paddingLeft: '0', paddingRight: '0'}}>
                                <Button size="large" variant="contained">Login</Button>
                                        
                                </ListItem>
                            </Grid>
                        </Grid>
                        <Grid item sx={{ width: '100%', margin: '.5rem 0'}}>
                            <Divider />
                            <ListItem sx={{display: 'flex', flexDirection: 'column', alignItems: 'center', paddingLeft: '0', paddingRight: '0'}}>
                                <Typography sx={{fontSize: '1.55rem', margin: '2rem 0'}} fontWeight='bold' >Não possui cadastro ainda ?</Typography>
                                <Button size="large" variant="outlined">Cadastre-se</Button> 
                            </ListItem>
                        </Grid>
                    </Grid>
                </Paper>
            </Container>
        </React.Fragment>
    )
}