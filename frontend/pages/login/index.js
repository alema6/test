
"use client";
import { useState } from "react";
import { useRouter } from "next/navigation";
import styles from "./logIn.module.css";
import { jwtDecode } from "jwt-decode"; // ← dodato

export default function Login() {
  const router = useRouter();

  const [form, setForm] = useState({ email: "", password: "" });

  const handleChange = (e) => {
    setForm({ ...form, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();

    try {
      const res = await fetch("http://localhost:8000/auth/login", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(form),
      });

      if (!res.ok) {
        const errorData = await res.json();
        alert("Error: " + errorData.detail);
        return;
      }

      const data = await res.json();
      alert("Login successful!");
      console.log("Access Token:", data.access_token);

      // Save token to localStorage
      localStorage.setItem("access_token", data.access_token);

      // Decode JWT token
      const decoded = jwtDecode(data.access_token);
      const userRole = decoded.role;
      localStorage.setItem("user_role", userRole);

      // Redirect based on role
      if (userRole === "admin") {
        router.push("/admin");
      } else {
        router.push("/");
      }
    } catch (error) {
      alert("Something went wrong.");
      console.error(error);
    }
  };

  return (
    <div className={styles.container}>
      <h2 className={styles.title}>Login</h2>
      <form onSubmit={handleSubmit} className={styles.form}>
        <input
          className={styles.input}
          name="email"
          type="email"
          placeholder="Email"
          value={form.email}
          onChange={handleChange}
          required
        />
        <br />
        <input
          className={styles.input}
          name="password"
          type="password"
          placeholder="Password"
          value={form.password}
          onChange={handleChange}
          required
        />
        <br />
        <button type="submit" className={styles.button}>
          Login
        </button>
      </form>
      <p className={styles.footer}>
        Don't have an account? <a href="/register">Register here</a>
      </p>
    </div>
  );
}
