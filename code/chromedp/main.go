package main

import (
	"context"
	"log"
	"os"
	"time"

	"github.com/chromedp/chromedp"
)

func main() {
	// Create a new context with headless mode enabled (default for chromedp.NewContext)
	ctx, cancel := chromedp.NewContext(context.Background())
	defer cancel()

	title := ""
	buf := []byte{}

	// Run tasks in the headless browser
	err := chromedp.Run(ctx,
		chromedp.Navigate("https://www.yelp.com/biz/andre-mechanic-toronto?adjust_creative=YyxvLuXxVUsYpEjpIYS-og&utm_campaign=yelp_api_v3&utm_medium=api_v3_business_search&utm_source=YyxvLuXxVUsYpEjpIYS-og"),
		chromedp.Title(&title),
		chromedp.CaptureScreenshot(&buf),
		chromedp.Sleep(2*time.Second), // Wait for the page to load
		// Add other actions here, e.g., capturing a screenshot or extracting data
	)
	if err != nil {
		log.Fatal(err)
	}
	log.Printf("Page Title: %s", title)

	os.WriteFile("screenshot.png", buf, 0644) // Save screenshot to file

	log.Printf("Screenshot captured, size: %d bytes", len(buf)) // Print first 100 bytes of the screenshot
}
