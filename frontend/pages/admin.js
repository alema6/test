"use client";
import { useEffect, useState } from "react";
import axios from "axios";
import { useRouter } from "next/navigation";

export default function AdminPanel() {
  const [korisnici, setKorisnici] = useState([]);
  const router = useRouter();

  useEffect(() => {
    const role = localStorage.getItem("user_role");
    if (role !== "admin") {
      alert("Pristup dozvoljen samo administratoru.");
      router.push("/");
    } else {
      fetchKorisnici();
    }
  }, []);

  const fetchKorisnici = async () => {
    const token = localStorage.getItem("access_token");

    const res = await axios.get("http://localhost:8000/users/za-odobrenje", {
      headers: {
        Authorization: `Bearer ${token}`,
      },
    });

    setKorisnici(res.data);
  };

  const odobri = async (id) => {
    const token = localStorage.getItem("access_token");

    await axios.put(`http://localhost:8000/users/odobri/${id}`, {}, {
      headers: {
        Authorization: `Bearer ${token}`,
      },
    });

    fetchKorisnici();
  };

  return (
    <div>
      <h2>Admin panel - Korisnici za odobrenje</h2>
      <ul>
        {korisnici.map((korisnik) => (
          <li key={korisnik.id}>
            {korisnik.username} ({korisnik.role}) - {korisnik.email}
            <button onClick={() => odobri(korisnik.id)}>Odobri</button>
          </li>
        ))}
      </ul>
    </div>
  );
}
