# Makhraj Auto World Product Requirement Document(PRD)

## Project Name

**Makhraj Auto World Website & Customer Management Platform**

**Version: 1.0**
**Author: Celestine Wangechi**
**Status: Draft**
**Last Updated: July 27, 2026**

---

## 1. Executive Summary

### Overview
Makhraj Auto world Website & Customer Management Platform is a modern web application designed to establish the garage's online presence while streamlining customer interactions, appointment booking and communication.
The platform will allow customers to discover services, schedule appointments, interact with an AI-powered assistant, and submit reviews. On the business side, administrators will manage appointments, customer reviews, and website content through an administrative dashboard.
The primary objective is to increase customer trust, improve operational efficiency, and generate more business through an intuitive digital experience.

---

## 2. Business Problem

Currently the garage has no website.

Potential customers cannot:

- Discover the garage online
- Learn about available services
- Book appointments
- View previous work
- Read customer reviews
- Contact the garage conveniently

Most communication happens manually through phone calls or WhatsApp, making appointment management inefficient and limiting business growth.

---

## 3. Goals

### Business Goals

- Establish a professional online presence.
- Increase appointment bookings.
- Improve customer trust.
- Reduce repetitive customer inquiries.
- Improve appointment management.
- Showcase completed work.
- Build an online reputation through customer reviews.

### User Goals

- Customers should be able to:
- Learn about the garage.
- Browse services.
- Book appointments.
- Contact the garage.
- Get answers instantly using AI chat.
- Leave reviews.

---

## 4. Success Metrics (KPIs)

- The platform will be considered successful if it achieves:
- Increase in online appointment bookings.
- Growth in customer reviews.
- Faster customer response time.
- Higher website traffic.
- Increased customer engagement.
- Reduced repetitive phone inquiries.

--

## 5. Target Users

### Primary Users

- Vehicle owners
- Returning customers
- New customers
- Fleet owners
- Business vehicle owners

### Secondary Users
- Garage administrators
- Mechanics
- Shop manager
- Business owner

## 6. User Personas

Persona 1 – Vehicle Owner
Name: James
Goal:
Find a trustworthy garage and book an appointment quickly.
Pain Points
Doesn't know which garages to trust.
Doesn't want to wait on phone calls.

Persona 2 – Returning Customer
Needs to:
Book another service
Contact the garage quickly

Persona 3 – Garage Administrator
Needs to:
Manage bookings
Respond to customers
Approve reviews
View orders

---

## 7. Functional Requirements

- Website
- The system shall provide:
- Home page
- About page
- Services page
- Gallery page
- Contact page
- FAQ page
- Booking page
- Booking System

### Customers shall be able to:
- Select service
- Choose preferred date
- Choose preferred time
- Enter vehicle information
- Describe the problem
- Submit booking

### System shall:
- Store booking
- Send confirmation email
- Notify administrator

### Administrator shall:
- Approve booking
- Reject booking
- Suggest alternative appointment times
- Mark booking completed

### The chatbot shall answer questions regarding:
- Service
- Booking
- Business hours
- Contact information
- Location
- Frequently asked questions
- The chatbot shall not invent information outside its knowledge base.
- Reviews

### Customers shall:
- Submit ratings
- Write reviews

### Administrator shall:
- Approve reviews
- Reject reviews
- Gallery

### Administrator shall:
- Upload photos
- Categorize images
- Remove images
- Contact

### Customers shall:
- Call
- Email
- Open WhatsApp
- View Google Maps
- Submit contact form

---

## 8. Non-Functional Requirements

### The application should be:

#### Responsive
- Desktop
- Tablet
- Mobile

#### Performance
- Fast page loading
- Optimized images
- Lazy loading where appropriate

#### Security
- HTTPS
- Password hashing
- JWT authentication for admins
- Input validation
- CSRF/XSS protection where applicable
- Secure file uploads

#### Reliability
- Booking data should never be lost.
- Graceful error handling.

#### Accessibility
- Keyboard navigation
- Good color contrast
- Semantic HTML
- Alt text for images

---

## 9. Pages
[] Home
[] About
[] Services
[] Gallery
[] Booking
[] Contact
[] FAQ
[] Admin Login
[] Dashboard

---

## 10. Admin Dashboard

### Modules:
- Dashboard
- Appointments
- Reviews
- Gallery
- FAQ
- Users (future)
- Analytics (future)

---

## 11. Integrations

- Google Maps
- WhatsApp
- Email Service
- AI API

---

## 12. Future Enhancements

- Customer accounts
- Loyalty program
- Vehicle service history
- Maintenance reminders
- Inventory management
- Mechanic scheduling
- SMS notifications
- Live appointment calendar
- AI-powered maintenance recommendations

---

## 13. Risks

- Risk	Mitigation
- Scope grows too much	Freeze MVP scope before development
- Chatbot gives incorrect answers -> Restrict responses to approved knowledge base
- Large image uploads -> Optimize and compress images
- Low initial reviews -> Allow review submissions and moderate them before publishing

---

## 14. Assumptions

- The client will provide branding assets (logo, colors, photos, videos)
- A business email is available for notifications.
- Business hours are fixed.
- The client will provide the physical location and Google Maps information.
- Delivery fees will follow business-defined rules.

---

## 15. Out of Scope (Version 1)
To keep the first release manageable, the following features are excluded:
- Multi-branch support
- Mechanic employee accounts
- Auto Shop
- Inventory forecasting
- Supplier management
- Customer loyalty program
- Native mobile applications
- Advanced business analytics
- Real-time mechanic availability tracking

---