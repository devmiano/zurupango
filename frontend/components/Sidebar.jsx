import Image from 'next/image';
import React from 'react';
import menuIcon from '../assets/icons/menu.svg';

const Sidebar = () => {
	return (
		<div id='sidebar'>
			<div className='menu'>
				<h3 className='text'>MENU</h3>
				<Image className='icon' src={menuIcon} alt='menu' />
			</div>
			<div className='links'>
				<a className='link' href=''>
					Locations
				</a>
			</div>

			<form className='search' action='' role='search'>
				<input
					className='input'
					type='text'
					name='search'
					id='search'
					placeholder='Search...'
					autoComplete='off'
				/>
				<button className='submit' type='submit'>
					search
				</button>
			</form>
			<div className='links'>
				<a href='/' className='link'>
					category
				</a>
			</div>
			<div className='links'>
				<p>No category available</p>
			</div>
		</div>
	);
};

export default Sidebar;
