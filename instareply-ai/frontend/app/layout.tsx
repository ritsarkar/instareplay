import type { Metadata } from "next";
import "./globals.css";

export const metadata: Metadata = {
  title: "InstaReply AI",
  description: "AI-powered Instagram DM automation for Indian businesses",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en">
      <body>{children}</body>
    </html>
  );
}
