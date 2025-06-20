// pages/register.js
"use client";
import { useState } from "react";
import { useRouter } from "next/navigation";
import styles from "./register.module.css";

export default function Register() {
  const router = useRouter();

  const [form, setForm] = useState({
    username: "",
    email: "",
    password: "",
    naziv_ime: "",
    adresa: "",
    broj: "",
    role: "user",
  });

  const handleChange = (e) => {
    setForm({ ...form, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();

    try {
      const res = await fetch("http://localhost:8000/auth/register", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(form),
      });

      if (!res.ok) {
        const errorData = await res.json();
        alert("Error: " + errorData.detail);
        return;
      }

      alert("Registration successful! Please login.");
      router.push("/login");
    } catch (error) {
      alert("Something went wrong.");
      console.error(error);
    }
  };

  return (
    <div className={styles.container}>
      <h2 className={styles.title}>Register</h2>
      <form onSubmit={handleSubmit} className={styles.form}>
        <input className={styles.input}
          name="username"
          placeholder="Username"
          value={form.username}
          onChange={handleChange}
          required
        />
        <br />
        <input className={styles.input}
          name="email"
          type="email"
          placeholder="Email"
          value={form.email}
          onChange={handleChange}
          required
        />
        <br />
        <input className={styles.input}
          name="password"
          type="password"
          placeholder="Password"
          value={form.password}
          onChange={handleChange}
          required
        />
        <br />
        <input className={styles.input}
          name="naziv_ime"
          placeholder="Naziv Ime"
          value={form.naziv_ime}
          onChange={handleChange}
          required
        />
        <br />
        <input className={styles.input}
          name="adresa"
          placeholder="Adresa"
          value={form.adresa}
          onChange={handleChange}
          required
        />
        <br />
        <input className={styles.input}
          name="broj"
          placeholder="Broj"
          value={form.broj}
          onChange={handleChange}
          required
        />
        <br />
        <select className={styles.input} name="role" value={form.role} onChange={handleChange}>
          <option value="user">User</option>
          <option value="shelter">Shelter</option>
          <option value="healthcare">Healthcare</option>
        </select>
        <br />
        <button type="submit" className={styles.button}>
          Register
        </button>
      </form>
      <p className={styles.footer}>
        Already have an account?{" "}
        <a href="/login" style={{ color: "blue", cursor: "pointer" }}>
          Login here
        </a>
      </p>
    </div>
  );
}
