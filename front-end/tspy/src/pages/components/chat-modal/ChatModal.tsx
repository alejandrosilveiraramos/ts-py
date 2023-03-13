

import * as React from 'react';
import Backdrop from '@mui/material/Backdrop';
import Box from '@mui/material/Box';
import Modal from '@mui/material/Modal';
import Fade from '@mui/material/Fade';
import Button from '@mui/material/Button';
import Typography from '@mui/material/Typography';

import facaMEI from '../../../shared/img/facaMEI.png'
import { CreateMei } from '../create-mei/CreateMei';


const style = {
  position: 'absolute' as 'absolute',
  top: '50%',
  left: '50%',
  transform: 'translate(-50%, -50%)',
  width: '80%',
  bgcolor: 'background.paper',
  border: '2px solid #e8e8e8',
  borderRadius: '1rem',
  boxShadow: 24,
  p: 4,
};


interface ChatModalProps {
    open: boolean;
    handleClose: () => void;
  }

export const ChatModal : React.FC<ChatModalProps> = ({ open, handleClose }) => {


  return (
    <div>
      <Modal
        aria-labelledby="transition-modal-title"
        aria-describedby="transition-modal-description"
        open={open}
        onClose={handleClose}
        closeAfterTransition
        slots={{ backdrop: Backdrop }}
        slotProps={{
          backdrop: {
            timeout: 500,
          },
        }}
      >
        <Fade in={open}>
          <Box sx={style}>
            <Typography id="transition-modal-title" variant="h4" component="h2" sx={{display: 'flex', alignItems: 'center', gap: '.2rem', margin: '2rem'}}>
            <img width={100} src={facaMEI} alt="Logo Faca MEI" /> Chat Fácil 
            </Typography> 
            <CreateMei />
          </Box>
        </Fade>
      </Modal>
    </div>
  );
}