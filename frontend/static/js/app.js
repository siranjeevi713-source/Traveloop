// Global Traveloop interactions

document.addEventListener('DOMContentLoaded', () => {
    // Handle active sidebar links
    const currentPath = window.location.pathname;
    const navLinks = document.querySelectorAll('.sidebar-nav a');
    
    navLinks.forEach(link => {
        if (link.getAttribute('href') === currentPath) {
            link.parentElement.classList.add('active');
        } else {
            link.parentElement.classList.remove('active');
        }
    });

    // Simple fade-in effect for main content
    const mainContent = document.getElementById('main-content');
    if (mainContent) {
        mainContent.classList.add('fade-in');
    }

    // Notification Dropdown Toggle
    const notifTrigger = document.getElementById('notif-trigger');
    const notifDropdown = document.getElementById('notif-dropdown');
    
    if (notifTrigger && notifDropdown) {
        notifTrigger.addEventListener('click', (e) => {
            e.stopPropagation();
            notifDropdown.classList.toggle('active');
            fetchNotifications();
        });
        
        document.addEventListener('click', () => {
            notifDropdown.classList.remove('active');
        });
        
        notifDropdown.addEventListener('click', (e) => e.stopPropagation());
    }

    async function fetchNotifications() {
        try {
            const response = await fetch('/api/notifications');
            const data = await response.json();
            const container = document.getElementById('notif-items');
            if (container && Array.isArray(data)) {
                if (data.length === 0) {
                    container.innerHTML = '<div style="padding: 20px; text-align: center; opacity: 0.5;">No notifications</div>';
                    return;
                }
                container.innerHTML = data.map(n => `
                    <div class="notif-item ${n.is_read ? '' : 'unread'}">
                        <div class="notif-icon ${n.type}"><i class="fas ${getNotifIcon(n.type)}"></i></div>
                        <div class="notif-content">
                            <h5>${n.title}</h5>
                            <p>${n.message}</p>
                            <span class="notif-time">${formatTime(n.created_at)}</span>
                        </div>
                    </div>
                `).join('');
            }
        } catch (err) { console.error('Failed to fetch notifications', err); }
    }

    function getNotifIcon(type) {
        switch(type) {
            case 'trip': return 'fa-plane';
            case 'budget': return 'fa-wallet';
            case 'activity': return 'fa-map-pin';
            default: return 'fa-info-circle';
        }
    }

    function formatTime(isoStr) {
        const date = new Date(isoStr);
        return date.toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' });
    }
});

// Helper for AJAX requests
const api = {
    async get(url) {
        const response = await fetch(url);
        return await response.json();
    },
    async post(url, data) {
        const response = await fetch(url, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(data)
        });
        return await response.json();
    }
};
