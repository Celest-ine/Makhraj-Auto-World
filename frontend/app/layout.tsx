import type { Metadata } from "next";
import "./globals.css";
export const metadata: Metadata={title:{default:"Makhraj Auto World",template:"%s | Makhraj Auto World"},description:"Explore Makhraj Auto World services and request vehicle service."};
export default function RootLayout({children}:Readonly<{children:React.ReactNode}>){return <html lang="en"><body>{children}</body></html>}
