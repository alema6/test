import React from 'react';
import Image from 'next/image';
import {Swiper, SwiperSlide} from 'swiper/react';
import{Navigation} from 'swiper';
import 'swiper/css/navigation';
import 'swiper/css';
import Service1Icon from '../public/img/services/service-icon1.svg';
import Service2Icon from '../public/img/services/service-icon2.svg';
import Service3Icon from '../public/img/services/service-icon3.svg';

const services=[
  {
    image: Service1Icon,
    name:'Tretmani',
    description:
    'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.',
    btnText:'Saznaj više'
  },

  {
    image: Service2Icon,
    name:'Frizure specifične za pasmine',
    description:
    'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.',
    btnText:'Saznaj više'
  },
  {
    image: Service3Icon,
    name:'Odjeća',
    description:
    'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.',
    btnText:'Saznaj više'
  
  }
];


const ServiceSlider = () => {
  return (
  <Swiper slidesPerView={1} spaceBetween={30} navigation={true} modules={[Navigation]} breakpoints={{
    768:{
      slidesPerView:2,
    },
  }}
  className='serviceSlider min-h-[680px]'
  
  >
    {services.map((service, index)=>{
      return(
      <SwiperSlide key={index} className='border border-primary/20 bg-cream min-h-[560px] rounded-[66px] py-16 px-8'>
      <Image className='mb-9' src={service.image} alt={service.name} />
      <div className='text-[26px] font-medium mb-4'>{service.name}</div>
      <div className='text-[20px] mb-8'>{service.description}</div>
      <button className='btn btn-primary'>{service.btnText}</button>
      </SwiperSlide>

      );
    })}
  </Swiper>);
};

export default ServiceSlider;
