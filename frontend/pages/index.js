import axios from "axios";
import Head from "next/head";
import { CatCard } from "../components";
import useFetch from "../utils/useFetch";
// import "../assets/scripts/cursor.js";

export default function Home({ cats }) {
  return (
    <>
      <Head>
        <title>Zurupango</title>
        <meta name="description" content="Generated by create next app" />
        <link rel="icon" href="/favicon.ico" />
        <link
          rel="stylesheet"
          href="https://cdnjs.cloudflare.com/ajax/libs/jquery-modal/0.9.1/jquery.modal.min.css"
        />
        <script src="https://cdnjs.cloudflare.com/ajax/libs/jquery-modal/0.9.1/jquery.modal.min.js"></script>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.0.0/jquery.min.js"></script>
      </Head>
      <section id="hero">
        <div className="banner">
          <div className="content">
            <h1 className="title">VISIT THE DEN</h1>
            <h1 className="subtitle">OF AFRICAS'</h1>
            <h1 className="title">BIGGEST CATS</h1>
          </div>
        </div>
      </section>
      <section id="section">
        <h1 class="stitle">Latest shots</h1>
        <div id="latest">
          {cats?.map((cat) => (
            <CatCard key={cat.id} cat={cat} />
          ))}
        </div>
      </section>
    </>
  );
}

export async function getServerSideProps() {
  const res = await axios.get(`http://127.0.0.1:8000/api/cats/`);
  const cats = res.data;

  return {
    props: { cats },
  };
}
