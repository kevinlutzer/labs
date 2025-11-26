package main

import (
	"context"
	"log"
	"time"

	"github.com/chromedp/chromedp"
)

func main() {
	// Create a new context with headless mode enabled (default for chromedp.NewContext)
	ctx, cancel := chromedp.NewContext(context.Background())
	defer cancel()

	title := ""

	// Run tasks in the headless browser
	err := chromedp.Run(ctx,
		chromedp.Navigate("https://www.google.com"),
		chromedp.Title(&title),
		chromedp.Sleep(2*time.Second), // Wait for the page to load
		// Add other actions here, e.g., capturing a screenshot or extracting data
	)
	if err != nil {
		log.Fatal(err)
	}
	log.Printf("Page Title: %s", title)
}
