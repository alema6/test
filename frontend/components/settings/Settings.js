"use client"
import React, {useState,useEffect} from "react";
import {LogOut, MessageSquare,Eye} from 'lucide-react';
import { useRouter } from 'next/navigation';

function Settings({isOpened,setIsOpened}){ 
    //provjera authentifikacije usera
    const [isAuth, setIsAuth] = useState(false);
    const router = useRouter();

    // useEffect(() => {
    //     setIsOpen(isOpened);
    // }, [isOpened]);

    useEffect(() => {
        const access_token= localStorage.getItem("access_token");
        if (access_token) {
            console.log(localStorage.getItem("access_token"));
            setIsAuth(true);
            console.log("logged");
        }
        //dark theme
        const theme = localStorage.getItem("theme");
        if (theme === "dark") {
            document.documentElement.classList.add("dark");
        } else {
            document.documentElement.classList.remove("dark");
        }
    }, []);

     const toggleDarkMode = () => {
        const isDark = document.documentElement.classList.toggle("dark");
        localStorage.setItem("theme", isDark ? "dark" : "light");
    };

    //logout opcija
    const logOut = () => {
        localStorage.removeItem("access_token");
        setIsAuth(false);
        toggleDarkMode();
        router.refresh();
    };
    const closingMenu = ()=> (
        setIsOpened(false)
    );

    return(        
        <ul onMouseLeave={closingMenu}
            className={`absolute right-3 mt-2 w-18 bg-white shadow-lg  transition-all duration-300 ease-in-out z-50  rounded-md
            ${isOpened ? 'opacity-100 translate-y-0 pointer-events-auto' : 'opacity-0 -translate-y-2 pointer-events-none '}
        `}>
                <li className={isAuth ? 'menuItem' : 'menuItem hidden' }><MessageSquare />Poruke</li>
                <li className='menuItem' onClick={toggleDarkMode}> <Eye className="dark:text-black"/> Tamni Nacin </li>
                <li onClick={logOut}  className={isAuth ? 'menuItem' : 'menuItem hidden' }> <LogOut  /> Odjava</li>
            </ul>
    
    );
}
     
export default Settings

