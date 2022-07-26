import React from 'react';
import { NavBrand, Footer, Sidebar } from '../components';

const Layout = ({ children }) => {
	return (
		<div id='app'>
			<div id='cursor' />
			<main id='main'>
				<NavBrand />
				<main className=''>{children}</main>
				<Footer />
			</main>
			<Sidebar />
		</div>
	);
};

export default Layout;
