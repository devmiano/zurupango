import React from 'react';
import '../styles/global.scss';
import Layout from '../utils/Layout';
import Script from 'next/script';
// import '../assets/scripts/cursor.js';

function MyApp({ Component, pageProps }) {
	return (
		<Layout>
			<Script src='https://cdnjs.cloudflare.com/ajax/libs/jquery/3.0.0/jquery.min.js' />
			<Script src='https://cdnjs.cloudflare.com/ajax/libs/jquery-modal/0.9.1/jquery.modal.min.js' />
			<Script src='cursor.js' />
			<Component {...pageProps} />
		</Layout>
	);
}

export default MyApp;
