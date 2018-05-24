// More info https://github.com/hakimel/reveal.js#configuration
    Reveal.initialize({
        controls: true,
        progress: true,
        history: true,
        center: true,

        transition: 'slide', // none/fade/slide/convex/concave/zoom

        // More info https://github.com/hakimel/reveal.js#dependencies
        dependencies: [
            { src: '/static/lib/js/classList.js', condition: function() { return !document.body.classList; } },
            { src: '/static/plugin/markdown/marked.js', condition: function() { return !!document.querySelector( '[data-markdown]' ); } },
            { src: '/static/plugin/markdown/markdown.js', condition: function() { return !!document.querySelector( '[data-markdown]' ); } },
            { src: '/static/plugin/highlight/highlight.js', async: true, callback: function() { hljs.initHighlightingOnLoad(); } },
            { src: '/static/plugin/search/search.js', async: true },
            { src: '/static/plugin/zoom-js/zoom.js', async: true },
            { src: '/static/plugin/notes/notes.js', async: true }
        ]
    });