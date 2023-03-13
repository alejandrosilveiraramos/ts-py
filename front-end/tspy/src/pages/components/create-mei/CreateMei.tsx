import React, { useEffect, useRef, useState }  from 'react';

import { Container, Divider, FormControl, Grid, IconButton, List, ListItem, ListItemText, Paper, TextField, Typography } from "@mui/material";
import { Box } from "@mui/system";


import './Chat.css';
import SendIcon from '@mui/icons-material/Send';


export const CreateMei: React.FC = () => {
    

  return (
        <React.Fragment>
            <Container>
                    <Box p={3} sx={{background: '#e8e8e8', borderRadius: '1rem'}}>
                        <Typography variant="h4" gutterBottom>
                            Abrir o MEI
                        </Typography>
                        <Divider />
                        <Grid container spacing={4} alignItems="center">
                            <Grid id="chat-window" lg={12} item>
                                <List id="chat-window-messages">
                                    {}
                                    <ListItem></ListItem>
                                </List>
                            </Grid>
                            <Grid lg={9} item>
                                <FormControl fullWidth>
                                    <TextField 
                                        
                                        label="Digite seu Primeiro Nome"
                                        variant="outlined"/>
                                </FormControl>
                            </Grid>
                            <Grid lg={1} item>
                                <IconButton 
                                    aria-label="send"
                                    color="primary">
                                        <SendIcon />
                                </IconButton>
                            </Grid>
                    
                        </Grid>
                    </Box>
            </Container>
        </React.Fragment>


  )

}