import React from 'react';
import Image from 'next/image';
import { formatDistance } from 'date-fns';

const CatDetail = ({ cat, location, category }) => {
	const { image, title, caption, posted } = cat;
	const { title: locationTitle } = location;
	const { title: categoryTitle, genus: categoryGenus } = category;

	return (
		<section id='detail'>
			<div class='shot'>
				<Image
					className='image'
					src={`https://res.cloudinary.com/devmiano/${image}`}
					alt={`${title}`}
					width={840}
					height={800}
				/>
			</div>
			<div class='content'>
				<h4 class='genus'>{categoryGenus}</h4>
				<p class='location'>{locationTitle}</p>
				<h1 class='title'>{title}</h1>
				<p class='caption'>{caption}</p>
				<p id='share'>{categoryTitle}</p>
				<div id='detail-cta'>
					<div class='date'>
						<p class='text'>Created:</p>
						<p class='posted'>
							{formatDistance(new Date(posted), new Date(), {
								addSuffix: true,
							})}
						</p>
					</div>
					<button id='copyLink' class='share'>
						Copy Link
					</button>
					<a class='close' href='/'>
						Close
					</a>
				</div>
			</div>
		</section>
	);
};

export const getStaticPaths = async () => {
	const res = await fetch('https://zurupango.herokuapp.com/api/cats/');
	const data = await res.json();

	const paths = data.map((cat) => ({
		params: {
			slug: String(cat.id),
		},
	}));

	return {
		paths,
		fallback: 'blocking',
	};
};

export const getStaticProps = async ({ params: { slug: id } }) => {
	const catres = await fetch(`https://zurupango.herokuapp.com/api/cat/${id}`);
	const cat = await catres.json();
	const locationres = await fetch(
		`https://zurupango.herokuapp.com/api/location/id/${(id = cat.location)}/`
	);
	const location = await locationres.json();
	const categoryres = await fetch(
		`https://zurupango.herokuapp.com/api/category/id/${(id = cat.category)}/`
	);
	const category = await categoryres.json();

	return {
		props: {
			cat,
			location,
			category,
		},
	};
};

export default CatDetail;
