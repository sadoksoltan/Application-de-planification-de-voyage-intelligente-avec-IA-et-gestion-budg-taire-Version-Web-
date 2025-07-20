export const routes = [
  {
    path: '/',
    name: 'home',
    component: () => import('pages/Home.vue')
  },
  {
    path: '/about',
    name: 'about',
    component: () => import('pages/About.vue')
  },
  {
    path: '/destination-list',
    name: 'destination-list',
    component: () => import('pages/destinations/DestinationList.vue')
  },
  {
    path: '/destination-detail',
    name: 'destination-detail',
    component: () => import('pages/destinations/DestinationDetail.vue')
  },
  {
    path: '/tour-list',
    name: 'tour-list',
    component: () => import('pages/tours/TourLists.vue')
  },
  {
    path: '/tour-grid',
    name: 'tour-grid',
    component: () => import('pages/tours/TourGrid.vue')
  },
  {
    path: '/tour-single',
    name: 'tour-single',
    component: () => import('pages/tours/TourSingle.vue')
  },
  {
    path: '/team',
    name: 'team',
    component: () => import('pages/Team.vue')
  },
  {
    path: '/booking',
    name: 'booking',
    component: () => import('pages/Booking.vue')
  },
  {
    path: '/confirmation',
    name: 'confirmation',
    component: () => import('pages/Confirmation.vue')
  },
  {
    path: '/services',
    name: 'services',
    component: () => import('pages/services/ServiceLists.vue')
  },
  {
    path: '/service-detail',
    name: 'service-detail',
    component: () => import('pages/services/ServiceDetail.vue')
  },
  {
    path: '/gallery1',
    name: 'gallery1',
    component: () => import('pages/GalleryMasonry.vue')
  },
  {
    path: '/404',
    name: 'error404',
    component: () => import('pages/Error404.vue')
  },
  {
    path: '/login',
    name: 'login',
    component: () => import('pages/Login.vue')
  },
  {
    path: '/register',
    name: 'register',
    component: () => import('pages/Register.vue')
  },
  {
    path: '/comingsoon',
    name: 'comingsoon',
    component: () => import('pages/ComingSoon.vue')
  },
  {
    path: '/testimonial',
    name: 'testimonial',
    component: () => import('pages/Testimonial.vue')
  },
  {
    path: '/contact',
    name: 'contact',
    component: () => import('pages/Contact.vue')
  },
  {
    path: '/faq',
    name: 'faq',
    component: () => import('pages/FAQ.vue')
  },
  {
    path: '/post-grid-1',
    name: 'post-grid-1',
    component: () => import('pages/blog/PostGrid1.vue')
  },
  {
    path: '/post-list-1',
    name: 'post-list-1',
    component: () => import('pages/blog/PostList1.vue')
  },
  {
    path: '/forgot-password',
    name: 'forgot-password',
    component: () => import('pages/forgot-password.vue')
  },
  {
    path: '/reset-password',
    name: 'reset-password',
    component: () => import('pages/reset-password.vue')
  },
  {
    path: '/dashboard',
    name: 'dashboard',
    component: () => import('pages/dashboard.vue')
  },
  {
    path: '/profile',
    name: 'profile',
    component: () => import('pages/Profile.vue')
  },
  {
    path: '/stats',
    name: 'stats',
    component: () => import('pages/stats.vue')
  },
  {
    path: '/users',
    name: 'users',
    component: () => import('pages/UsersList.vue')
  },
  {
    path: '/users/create',
    name: 'users_create',
    component: () => import('pages/UserCreate.vue')
  },
  {
    path: '/admin/tours',
    name: 'admin-tours',
    component: () => import('pages/TourAdminList.vue')
  },
  {
    path: '/admin/tours/create',
    name: 'admin-tours-create',
    component: () => import('pages/TourAdminCreate.vue')
  },
  {
    path: '/admin/posts',
    name: 'PostAdminList',
    component: () => import('pages/PostAdminList.vue')
  },
  {
    path: '/admin/posts/create',
    name: 'PostCreate',
    component: () => import('pages/PostCreate.vue')
  },
  {
    path: '/admin/tours/:id',
    name: 'TourEdit',
    component: () => import('pages/TourEdit.vue')
  },
  {
    path: '/admin/posts/:id',
    name: 'PostEdit',
    component: () => import('pages/PostEdit.vue')
  },
  {
    path: '/admin/reservations',
    name: 'reservations',
    component: () => import('pages/AllReservations.vue')
  },
  {
    path: '/bookings/calendar',
    name: 'BookingsCalendar',
    component: () => import('pages/BookingsCalendar.vue')
  },
  {
    path: '/travel-ia-tunisia',
    name: 'TravelIATunisia',
    component: () => import('pages/TravelIATunisiaView.vue')
  }
]
