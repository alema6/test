import React,{useState,useEffect} from 'react';
import Image from 'next/image';
import Logo from '../public/img/header/logo.svg';
import { useRouter } from 'next/router';
import SettingsDropdown from './settings/SettingsIcon';
const Header = () => {

  const router = useRouter();
  const [isAuth, setIsAuth] = useState(false);

  useEffect(() => {
    const access_token = localStorage.getItem("access_token");
    if (access_token) {
      console.log(localStorage.getItem('access_token'));
        setIsAuth(true);
        console.log("logged");
    }
  }, []);

  return(
  <header className='py-6 lg:absolute lg:w-full lg:left-0'>
    <div className='container mx-auto flex flex-col gap-y-6 lg:flex-row h-full justify-between items-center relative'>
      <a href="#">
        <Image src={Logo}/>
      </a>
      <nav className='text-xl flex gap-x-4 lg:gap-x-12'>
        <a href="#">Usluge</a>
        <a href="#">O nama</a>
        <a href="#">Kontakt</a>
      </nav>
      <button className={!isAuth ? 'btn btn-primary-l lg:btn-outline-l' : 'btn hidden'} onClick={()=> router.push('/login')}>Log in</button>
      <button className={!isAuth ? 'btn btn-primary lg:btn-outline': 'btn hidden'} onClick={() => router.push('/register')} >Register</button>
      <SettingsDropdown />

      
      
    </div>
  </header>
);
};

export default Header;

//<div className={!isAuth ? styles.headerButton : styles.headerButtonInv}> 


