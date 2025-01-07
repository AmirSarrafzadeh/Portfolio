(function () {
    "use strict";

    /**
     * Easy selector helper function
     */
    const select = (el, all = false) => {
        el = el.trim();
        if (all) {
            return [...document.querySelectorAll(el)];
        } else {
            return document.querySelector(el);
        }
    };

    /**
     * Easy event listener function
     */
    const on = (type, el, listener, all = false) => {
        let selectEl = select(el, all);
        if (selectEl) {
            if (all) {
                selectEl.forEach(e => e.addEventListener(type, listener));
            } else {
                selectEl.addEventListener(type, listener);
            }
        }
    };

    /**
     * Easy on scroll event listener
     */
    const onscroll = (el, listener) => {
        el.addEventListener('scroll', listener);
    };

    /**
     * Navbar links active state on scroll
     */
    let navbarlinks = select('#navbar .scrollto', true);
    const navbarlinksActive = () => {
        let position = window.scrollY + 200;
        navbarlinks.forEach(navbarlink => {
            if (!navbarlink.hash) return;
            let section = select(navbarlink.hash);
            if (!section) return;
            if (position >= section.offsetTop && position <= (section.offsetTop + section.offsetHeight)) {
                navbarlink.classList.add('active');
            } else {
                navbarlink.classList.remove('active');
            }
        });
    };
    window.addEventListener('load', navbarlinksActive);
    onscroll(document, navbarlinksActive);

    /**
     * Scrolls to an element with header offset
     */
    const scrollto = (el) => {
        let elementPos = select(el).offsetTop;
        window.scrollTo({
            top: elementPos,
            behavior: 'smooth'
        });
    };

    /**
     * Back to top button
     */
    let backtotop = select('.back-to-top');
    if (backtotop) {
        const toggleBacktotop = () => {
            if (window.scrollY > 100) {
                backtotop.classList.add('active');
            } else {
                backtotop.classList.remove('active');
            }
        };
        window.addEventListener('load', toggleBacktotop);
        onscroll(document, toggleBacktotop);
    }

    /**
     * Mobile nav toggle
     */
    on('click', '.mobile-nav-toggle', function () {
        const body = select('body');
        const header = select('#header');
        const toggle = select('.mobile-nav-toggle');

        // Toggle classes for navigation
        body.classList.toggle('mobile-nav-active');
        header.classList.toggle('mobile-nav-active');

        // Update the toggle button icon
        toggle.classList.toggle('bi-list');
        toggle.classList.toggle('bi-x');
    });

    /**
     * Close mobile nav when clicking outside
     */
    document.addEventListener('click', function (e) {
        const body = select('body');
        const header = select('#header');
        const toggle = select('.mobile-nav-toggle');

        // Close nav if clicking outside
        if (body.classList.contains('mobile-nav-active') &&
            !e.target.closest('#header') &&
            !e.target.closest('.mobile-nav-toggle')) {
            body.classList.remove('mobile-nav-active');
            header.classList.remove('mobile-nav-active');

            // Reset toggle button icon
            toggle.classList.add('bi-list');
            toggle.classList.remove('bi-x');
        }
    });


    /**
     * Scroll with offset on links with a class name .scrollto
     */
    on('click', '.scrollto', function (e) {
        if (select(this.hash)) {
            e.preventDefault();
            const body = select('body');
            const navbarToggle = select('.mobile-nav-toggle');
            if (body.classList.contains('mobile-nav-active')) {
                body.classList.remove('mobile-nav-active');
                navbarToggle.classList.add('bi-list');
                navbarToggle.classList.remove('bi-x');
                select('#header').classList.remove('mobile-nav-active');
            }
            scrollto(this.hash);
        }
    }, true);

    /**
     * Scroll with offset on page load with hash links in the URL
     */
    window.addEventListener('load', () => {
        if (window.location.hash) {
            if (select(window.location.hash)) {
                scrollto(window.location.hash);
            }
        }
    });

    /**
     * Hero type effect
     */
    const typed = select('.typed');
    if (typed) {
        let typed_strings = typed.getAttribute('data-typed-items');
        typed_strings = typed_strings.split(',');
        new Typed('.typed', {
            strings: typed_strings,
            loop: true,
            typeSpeed: 100,
            backSpeed: 50,
            backDelay: 2000
        });
    }

    /**
     * Animation on scroll
     */
    window.addEventListener('load', () => {
        AOS.init({
            duration: 1000,
            easing: 'ease-in-out',
            once: true,
            mirror: false
        });
    });

    /**
     * Initiate Pure Counter
     */
    new PureCounter();

})();
