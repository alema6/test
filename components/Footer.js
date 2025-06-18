import React from 'react';
import {BsFacebook,BsInstagram, BsTwitter} from 'react-icons/bs';


const Footer = () => {
  return (
  <footer className='bg-footer bg-cover bg-center bg-no-repeat min-h-[263px] flex items-center py-8'>
    <div className='container mx-auto'>
      <div className='flex flex-col lg:flex-row justify-between'>
        <div className='flex-1 text-orange text-4xl text-center lg:text-left flex items-center justify-center lg:justify-start mb-6'>Životinje na prvom mjestu</div>
        <div className='text-white flex-1'>
          <ul className='flex flex-col gap-y-6 items-center lg:flex-row lg:gap-x-4 text-base font-semibold mb-8'>
            <li><a href='#'>Usluge</a></li>
            <li><a href='#'>O nama</a></li>
            <li><a href='#'>Kontakt</a></li>
            

          </ul>
          <div className='flex justify-center lg:justify-start'>
            <div className='mr-6'>Zapratite nas</div>
            <ul className='flex gap-x-4'>
              <li><a href='https://www.facebook.com/'><BsFacebook/></a></li>
              <li><a href='https://www.instagram.com/'><BsInstagram/></a></li>
              <li><a href='https://x.com/'><BsTwitter/></a></li>
            </ul>
          </div>
        </div>
      </div>
    </div>
  </footer>

  );
};

export default Footer;
