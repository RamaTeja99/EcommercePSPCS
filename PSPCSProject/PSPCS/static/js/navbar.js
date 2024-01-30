function toggleSearch() {
    var searchForm = document.querySelector('.search-form');
    searchForm.style.display = (searchForm.style.display === 'none' || searchForm.style.display === '') ? 'flex' : 'none';
}
