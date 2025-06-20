"use client"
import React, { useState } from 'react';
import { CircleChevronDown } from 'lucide-react'; //bibiloteka za ikonice
import Settings from './Settings';


function SettingsDropdown() {

    const [isOpen, setIsOpen] = useState(false);
    const [isHover, setIsHover] = useState(false);
    const settingsClick = () =>(
      setIsOpen(!isOpen)
    );

    const settsHover = () => (
      setIsHover(true)
    );
    const settsNotHover = () => (
      setIsHover(false)
    );

    return(
      <div className="px-4 py-2">    
        <div onClick={settingsClick} onMouseOver={settsHover} onMouseOut={settsNotHover} style={{ cursor: "pointer" }} > 
           <CircleChevronDown color={isHover ? 'white' : 'orange'} size={50}/>
        </div>
        <Settings isOpened={isOpen} setIsOpened={setIsOpen}></Settings>     
      </div>
      
    );

}
 export default SettingsDropdown
