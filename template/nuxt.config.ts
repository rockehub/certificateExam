// https://nuxt.com/docs/api/configuration/nuxt-config

export default defineNuxtConfig({
 devtools: {enabled: true},

 typescript: {
					shim: false,
	},

 ssr: false,

 app: {
					head: {
									title: "Exame de Certificação",
									charset: 'utf-8',
									viewport: 'width=device-width, initial-scale=1',
									script: [
													{
																	src: "https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js",
													},
									],
					}
	},

 css: [
					"bootstrap/scss/bootstrap.scss",
					"@/assets/css/font-awesome-pro.css",
					"@/assets/css/flaticon_shofy.css",
					"@/assets/scss/main.scss",
	],

 compatibilityDate: "2025-03-06",
});