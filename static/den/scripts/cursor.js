(() => {
	const cursor = document.getElementById('cursor');

	document.addEventListener('mousemove', (e) => {
		cursor.setAttribute(
			'style',
			`top:  ${e.pageY - 20}px; 
      left: ${e.pageX - 20}px;`
		);
	});

	document.addEventListener('click', () => {
		cursor.classList.add('cursor--expand');

		setTimeout(() => {
			cursor.classList.remove('cursor--expand');
		}, 500);
	});
})();
