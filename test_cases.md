# SauceDemo E2E Test Cases

## Authentication

### TC01 - Login with valid credentials
Expected: User is logged in and Products page is displayed.

### TC02 - Login with invalid password
Expected: Login fails and an error message is displayed.

### TC03 - Login with locked-out user
Expected: Login is blocked and a locked-out error is displayed.

## Cart

### TC04 - Add a single product to cart
Expected: Product is added and cart count becomes 1.

### TC05 - Add multiple products to cart
Expected: Selected products are added and cart count matches the number of products.

### TC06 - Remove a product from cart
Expected: Product is removed from the cart.

### TC07 - Verify cart contents
Expected: Cart displays the correct product name, price and quantity.

## Checkout

### TC08 - Complete checkout with valid information
Expected: Checkout completes and order confirmation is displayed.

### TC09 - Checkout with missing required information
Expected: Checkout is prevented and a validation error is displayed.

## Session

### TC10 - Logout successfully
Expected: User is logged out and returned to the login page.