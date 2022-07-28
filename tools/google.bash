google() {
	search=""
	echo "Googling: $@"
	for term in $@; do
		search="$search%20$term"
	done
	xdg-open "https://www.google.com/search?=$search"
}

