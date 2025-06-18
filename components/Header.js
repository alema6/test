import React from 'react';
import Image from 'next/image';
import Logo from '../public/img/header/logo.svg';
const Header = () => {
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
      <button className='btn btn-primary lg:btn-outline'>Sign up</button>
      <button className='btn btn-primary lg:btn-outline'>Register</button>
    </div>
  </header>
);
};

export default Header;
