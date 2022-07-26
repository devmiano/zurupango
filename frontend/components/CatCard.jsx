import React from 'react';
import Image from 'next/image';
import Link from 'next/link';

const CatCard = ({ cat: { id, title, image, location, category } }) => {
	return (
		<>
			<a href={`#${id}`} id='cat' rel='modal:open'>
				<div className='wrapper'>
					<Image
						className='image'
						src={`https://res.cloudinary.com/devmiano/${image}`}
						alt={`${title}`}
						width={800}
						height={500}
					/>
				</div>
				<div className='content'>
					<div className='top'>
						<p className='location'>{title}</p>
						<p className='category'>{title}</p>
					</div>
					<h4 className='title'>{title}</h4>
				</div>
			</a>
			<div id={`${id}`} className='modal cat-modal'>
				<a id='cat' href='/'>
					<div className='wrapper'>
						<Image
							className='image'
							src={`https://res.cloudinary.com/devmiano/${image}`}
							alt={`${title}`}
							width={800}
							height={500}
						/>
					</div>
					<div className='content'>
						<div className='top'>
							<p className='location'>{location}</p>
							<p className='category'>{category}</p>
						</div>
						<h4 className='title'>{title}</h4>
					</div>
				</a>
				<div id='cta'>
					<Link href={`/cat/${id}`}>
						<div className='share'>Details</div>
					</Link>
					<a className='close' href='#' rel='modal:close'>
						Close
					</a>
				</div>
			</div>
		</>
	);
};

export default CatCard;
