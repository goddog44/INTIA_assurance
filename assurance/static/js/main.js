// Initialize the application when DOM is loaded
document.addEventListener('DOMContentLoaded', function() {
    // Set the active tab based on current URL
    const path = window.location.pathname;
    if (path.includes('clients')) {
        document.querySelector('[data-tab="clients"]').classList.add('text-primary', 'border-primary');
        document.querySelector('[data-tab="clients"]').classList.remove('text-gray-500', 'dark:text-gray-400', 'border-transparent');
    } else if (path.includes('insurances')) {
        document.querySelector('[data-tab="insurances"]').classList.add('text-primary', 'border-primary');
        document.querySelector('[data-tab="insurances"]').classList.remove('text-gray-500', 'dark:text-gray-400', 'border-transparent');
    }
    
    // Set the current branch name in header
    const branchName = document.querySelector('meta[name="branch-name"]').content;
    if (branchName) {
        document.getElementById('userBranch').textContent = branchName;
        document.getElementById('userBranch').classList.remove('hidden');
    }
});

// Format dates in tables
function formatTableDates() {
    document.querySelectorAll('.date-cell').forEach(cell => {
        if (cell.textContent) {
            const date = new Date(cell.textContent);
            cell.textContent = date.toLocaleDateString('fr-FR');
        }
    });
}

// Call this function when page loads
formatTableDates();