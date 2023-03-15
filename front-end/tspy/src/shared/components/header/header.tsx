import React, { useState } from 'react';

import {AppBar , Box, Toolbar, Typography, Button, Container, Menu, MenuItem, Tooltip, Avatar, ThemeProvider} from '@mui/material';

import IconButton from '@mui/material/IconButton';
import MenuIcon from '@mui/icons-material/Menu';
import { Link } from 'react-router-dom';

import  theme from '../../theme/Theme';
import facaMEI from '../../img/facaMEI.png'


/* import avatarImg from '../../../assets/img/avatar.jpeg'; */

interface HeaderMenuItems {
  text: string;
  path: string;
}

export const Header = () => {

  const pages: HeaderMenuItems[] = [
    {
      text: 'Página Principal',
      path: '/'
    },
    {
      text: 'Informação',
      path: '/login'
    },
    {
      text: 'Sobre',
      path: '/login'
    },
    {
      text: 'Contato',
      path: '/login'
    },
    {
      text: 'Login',
      path: '/login'
    },
  ];
  const settings = ['Profile', 'Account', 'Dashboard', 'Logout'];

  const [selectedTab, setSelectedTab] = useState<number>(0);

  const [anchorElNav, setAnchorElNav] = React.useState<null | HTMLElement>(null);
  const [anchorElUser, setAnchorElUser] = React.useState<null | HTMLElement>(null);

  const handleOpenNavMenu = (event: React.MouseEvent<HTMLElement>) => {
    setAnchorElNav(event.currentTarget);
  };
  const handleOpenUserMenu = (event: React.MouseEvent<HTMLElement>) => {
    setAnchorElUser(event.currentTarget);
  };
  
  const handleCloseNavMenu = () => {
    setAnchorElNav(null);
  };

  const handleCloseUserMenu = () => {
    setAnchorElUser(null);
  };
  const handleTabChange = (event: React.SyntheticEvent, newValue: number) => {
    setSelectedTab(newValue);
  };

  const handleMenuItemClick = (event: React.MouseEvent<HTMLElement>, path: string, newValue: number) => {
    handleCloseNavMenu();
    handleTabChange(event, newValue);
  }


      
  return (
    <ThemeProvider theme={theme}>
    <AppBar position="static" sx={{ background: '#fff'}}>
      <Container  maxWidth="xl" >
        <Toolbar disableGutters >
          <img width={100} src={facaMEI} alt="Logo Faca MEI" />
          <Box sx={{ flexGrow: 1, display: { xs: 'flex', md: 'none' } }}>
            <IconButton
              size="large"
              aria-label="account of current user"
              aria-controls="menu-appbar"
              aria-haspopup="true"
              onClick={handleOpenNavMenu}
            >
              <MenuIcon />
            </IconButton>
            <Menu
              id="menu-appbar"
              anchorEl={anchorElNav}
              anchorOrigin={{
                vertical: 'bottom',
                horizontal: 'left',
              }}
              keepMounted
              transformOrigin={{
                vertical: 'top',
                horizontal: 'left',
              }}
              open={Boolean(anchorElNav)}
              onClose={handleCloseNavMenu}
              sx={{
                display: { xs: 'block', md: 'none' },
              }}
            >
              {pages.map((page, index) => (
                <MenuItem  
                    key={index}  
                    component={Link}
                    to={page.path}
                    onClick={(event) => handleMenuItemClick(event, page.path, index)}
                    sx={{ color: 'blue' }}
                >
                  <Typography  textAlign="center">{page.text} </Typography>
                </MenuItem>
              ))}
            </Menu>
          </Box>
          {/* <AirplanemodeActiveIcon sx={{ display: { xs: 'flex', md: 'none' }, mr: 1 }} /> */}

          <Box sx={{ flexGrow: 1, display: { xs: 'none', md: 'flex' }, justifyContent: 'center' }}>
            {pages.map((page, index) => (
              <Button
              key={index}  component={Link} to={page.path} onClick={(event) => handleMenuItemClick(event, page.path, index)} sx={{ my: 2, color: '#000', fontSize: '1.5rem', textDecoration: 'none'}}
              >
                {page.text}
              </Button>
            ))}
          </Box>

          <Box sx={{ flexGrow: 0 }}>
            <Tooltip title="Open settings">
              <IconButton onClick={handleOpenUserMenu} sx={{ p: 0 }}>
                <Avatar alt="Remy Sharp"  />
              </IconButton>
            </Tooltip>
            <Menu
              sx={{ mt: '45px' }}
              id="menu-appbar"
              anchorEl={anchorElUser}
              anchorOrigin={{
                vertical: 'top',
                horizontal: 'right',
              }}
              keepMounted
              transformOrigin={{
                vertical: 'top',
                horizontal: 'right',
              }}
              open={Boolean(anchorElUser)}
              onClose={handleCloseUserMenu}
            >
              {settings.map((setting) => (
                <MenuItem key={setting} onClick={handleCloseUserMenu}>
                  <Typography textAlign="center">{setting}</Typography>
                </MenuItem>
              ))}
            </Menu>
          </Box>
        </Toolbar>
      </Container>
    </AppBar>
    </ThemeProvider>
    )
}