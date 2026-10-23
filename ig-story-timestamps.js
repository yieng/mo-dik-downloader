const sleep = (ms) => new Promise(resolve => setTimeout(resolve, ms));

async function trackTimeElement() {
  let count = 0;

  // Runs the loop 5 times (change this condition as needed)
  while (count < 10000) {
    // 1. Fetch the element and its attribute
    const timeElement = document.querySelector("time");
    
    if (timeElement) {
      const currentDateTime = timeElement.dateTime;
      console.log(currentDateTime);
    } else {
      console.log(`Iteration ${count + 1}: <time> element not found on page.`);
    }

    // 2. Wait 3 seconds before continuing
    await sleep(3000);
    
    count++;
  }
}

// Execute the loop
trackTimeElement();