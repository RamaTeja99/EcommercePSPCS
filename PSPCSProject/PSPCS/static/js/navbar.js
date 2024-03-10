function toggleSearch() {
    var searchForm = document.querySelector('.navbar .d-flex');
    if (searchForm.style.display === 'none' || searchForm.style.display === '') {
        searchForm.style.display = 'flex';
    } else {
        searchForm.style.display = 'none';
    }
}
