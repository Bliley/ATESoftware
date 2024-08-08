import javax.swing.*;
import javax.swing.plaf.FontUIResource;
import java.awt.*;
import java.awt.event.*;
import java.io.File;
import java.io.IOException;
import java.sql.*;
import java.time.LocalDate;
import java.time.temporal.WeekFields;
import java.util.ArrayList;
import java.util.Enumeration;

public class LaserMarker extends JFrame {
    // TODO: Refactor variable and function names, put any code that is repeated multiple times into a function,
    //  add comments, get rid of unused code, add GUI buttons for increased usability
    private int pSerialNumber;                                                                                          // For printing the serial number
    private String workOrderInput;
    private int itemQuantity;                                                                                           // How many items are in a work order
    private int partsLeft;                                                                                              // Tracks how many parts are left TODO: fix the partsLeft so it updates after every batch
    private int fixtureCapacity;                                                                                        // User enters fixture capacity
    private String fixture;                                                                                             // The fixture that gets displayed for user
    private int totalBatches;                                                                                           // Calculates total number of batches based off of the "partsLeft" column in the ETCHER_TRACKER DB
    private int currentBatch = 1;                                                                                       // Keeps track of the current batch
    private Connection connectionX;                                                                                     // Connection to Xtuple
    private Connection connectionA;                                                                                     // Connection to AppleCore
    LocalDate currentDate = LocalDate.now();                                                                            // Current data
    String currentYear = String.valueOf(currentDate.getYear() % 100);                                                 // Current year as a 2 digit value for DCSN
    String currentWeek = String.valueOf(currentDate.get(WeekFields.ISO.weekOfWeekBasedYear()));                         // Current week for DCSN
    private final ArrayList<Product> productList = new ArrayList<>();                                                   // productList is where each DCSN is being stored into
    private boolean existsInDatabase;                                                                                   // Work Order validation
    private Robot robot;                                                                                                // Java's robot class for keystroke implementation
    // TESTING VARIABLES
    private JComboBox<String> fileDropdown;
    private JButton selectButton;
    private String selectedFilePath;

    public LaserMarker() {                                                                                              // Class constructor
        setTitle("Laser Engraver GUI");                                                                                 // Title for the GUI frame
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);                                                                 // Ends the program when user closes the GUI
        setLayout(new GridBagLayout());                                                                                 // GridBayLayout manager for orientation
        connectXtupleReal();                                                                                            // Connecting to Xtuple database
        connectAppleCore();                                                                                             // Connecting to Applecore database

        try {
            robot = new Robot();                                                                                        // Creating a Robot object
        } catch (AWTException e) {
            e.printStackTrace();
        }

        scanOrderPanel();                                                                                               // Show the scan order panel first

        pack();                                                                                                         // Pack the components together
        setLocationRelativeTo(null);                                                                                    // Center the frame on the screen
        setVisible(true);                                                                                               // Make the frame visible
    }

    /**
     * User prompt to enter the Work Order Number
     */
    private void scanOrderPanel() {
        JLabel workOrderLabel = new JLabel("Scan Work Order: ");                                                   // Prompt user to scan work order
        JTextField workOrderNumberField = new JTextField(10);                                                   // Text field for user's input TODO: Change name to workOrderNumberTextField
        JButton okButton = new JButton("OK");                                                                      // OK button for scanning work order number

        // validating the user input (testing phase)
        okButton.addActionListener(e -> {
            workOrderInput = workOrderNumberField.getText();                                                            // workOrderInput keeps track of the user's input for the work order text field
            retrieveWorkOrderInformation(workOrderInput);                                                               // Calling the function to retrieve the wo_quantity, item number, etc. for the user's input
            if(existsInDatabase){
                verifyOrderPanel();                                                                                     // only if user's entered work order exists in the database then go to the verify order panel
            }
        });

        GridBagConstraints gbc = new GridBagConstraints();                                                              // For GUI component layout purposes

        gbc.gridx = 0;                                                                                                  // Sets the row index
        gbc.gridy = 0;                                                                                                  // Sets the column index
        gbc.insets = new Insets(10, 10, 10, 10);                                                   // External padding (insets) around the component being added
        add(workOrderLabel, gbc);                                                                                       // Work order label is added to the first column and first row (0,0)
        add(workOrderNumberField);                                                                                      // Adding to scan order panel

        gbc.gridx = 2;                                                                                                  // Redefining the x location to the 3rd row (position 2)
        add(okButton, gbc);                                                                                             // Adding the "Ok" button to the panel
    }

    private void verifyOrderPanel() {


        JLabel verifyLabel = new JLabel("Work order received: " + workOrderInput);
        JButton nextButton = new JButton("Next");
        nextButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                // push the work order to the ETCHER_TRACKER table in AppleCore
                // if the work order is already in there then it will take it and append to it, otherwise, add a new work order
                grabFixturePanel();
            }
        });

        getContentPane().removeAll();
        add(verifyLabel);
        add(nextButton);
        revalidate();
        repaint();
    }

    private void grabFixturePanel(){

        // Create the fixture capacity components
        JComboBox<Integer> enterFixtureQuantity = new JComboBox<>();
        for (int i = 1; i <= 40; i++) {
            enterFixtureQuantity.addItem(i);
        }
        JLabel enterFixQtyLabel = new JLabel("Enter fixture capacity: ");
        JLabel fillFixtureLabel = new JLabel("Fill fixture with batch: " + currentBatch + " of " + totalBatches);
        JCheckBox batchCheckBox = new JCheckBox("Batch " + currentBatch + " is filled.");
        JButton nextButton = new JButton("Next");
        nextButton.setEnabled(false);   // Disable the Next button initially

        // Add an ItemListener to the checkbox
        batchCheckBox.addItemListener(e -> {
            nextButton.setEnabled(e.getStateChange() == ItemEvent.SELECTED);    // Enable or disable the Next button based on the checkbox state
        });

        // Add an ActionListener to the Next button
        nextButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                enteringDCSN();
                // placeFixturePanel();
            }
        });

        // Create the components
        fileDropdown = new JComboBox<>();                                                                               // Drop down for user's selected Laser Program
        fileDropdown.setPreferredSize(new Dimension(300,30));
        selectButton = new JButton("Select Program");

        // Configure the select button action listener
        selectButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                JFileChooser fileChooser = new JFileChooser();

                // Set the default directory to "Downloads"
                String userHome = System.getProperty("user.home");
                String downloadsPath = "\\C:\\Users\\Laser Marker\\Desktop\\Crystal Cans with QR";  // TODO: Change this to the laser engraver files (\\MAIL01\Engr_Docs\Laser Marker\Marking Builder 3\Program\By Assembly)
                File downloadsDir = new File(downloadsPath);
                fileChooser.setCurrentDirectory(downloadsDir);

                // Set Dimensions
                Dimension dialogSize = new Dimension(800, 600);
                fileChooser.setPreferredSize(dialogSize);

                int result = fileChooser.showOpenDialog(LaserMarker.this);
                if (result == JFileChooser.APPROVE_OPTION) {
                    File selectedFile = fileChooser.getSelectedFile();
                    String filePath = selectedFile.getAbsolutePath();

                    // Store the selected file path in a variable
                    selectedFilePath = filePath;

                    // Use the selectedFilePath variable as needed
                    System.out.println("Selected File: " + selectedFilePath);

                    fileDropdown.addItem(filePath);
                    fileDropdown.setSelectedItem(filePath);
                }
            }
        });

        // Listen for selection changes in the fixture quantity dropdown
        enterFixtureQuantity.addItemListener(e -> {
            if (e.getStateChange() == ItemEvent.SELECTED) {
                fixtureCapacity = (int) enterFixtureQuantity.getSelectedItem();
                partsLeft = getPartsLeft(workOrderInput);
                totalBatches = calculateTotalBatches(partsLeft, fixtureCapacity); // Calculate the total number of batches

                // Update the fillFixtureLabel with the new totalBatches value
                fillFixtureLabel.setText("Fill fixture with batch: " + currentBatch + " of " + totalBatches);

                enterFixtureQuantity.removeItemListener((ItemListener) this);
            }
        });



        getContentPane().removeAll();
        // Add components to the fixturePanel. The Y- coordinate determines the order that the components are being shown vertically
        GridBagConstraints gbc = new GridBagConstraints();
        gbc.gridx = 0;
        gbc.gridy = 0;
        gbc.insets = new Insets(10, 10, 10, 10);
        add(fileDropdown);
        gbc.gridy = 1;
        add(selectButton, gbc);
        gbc.gridy = 2;
        add(enterFixQtyLabel, gbc);
        gbc.gridx = 1;
        add(enterFixtureQuantity, gbc);
        gbc.gridx = 0;
        gbc.gridy = 3;
        add(fillFixtureLabel, gbc);
        gbc.gridy = 4;
        add(batchCheckBox, gbc);
        gbc.gridy = 5;
        add(nextButton, gbc);

        revalidate();
        repaint();
    }

    public void placeFixturePanel(){
        JLabel batchLabel = new JLabel("Place batch: " + currentBatch + " into position");
        JLabel focusLabel = new JLabel("Focus the laser");
        JButton focusButton = new JButton("Focus Laser");
        JCheckBox laserCheck = new JCheckBox("Laser is focused");
        JButton nextButton = new JButton("Next");
        nextButton.setEnabled(false);   // Disable the Next button initially

        // Add an ItemListener to the checkbox
        laserCheck.addItemListener(new ItemListener() {
            @Override
            public void itemStateChanged(ItemEvent e) {
                nextButton.setEnabled(e.getStateChange() == ItemEvent.SELECTED);    // Enable or disable the Next button based on the checkbox state
            }
        });

        focusButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                // Switching back to the laser app to focus the laser
                try {
                    Thread.sleep(50);
                } catch (InterruptedException ex) {
                    throw new RuntimeException(ex);
                }
                robot.keyPress(KeyEvent.VK_ALT);
                try {
                    Thread.sleep(50);
                } catch (InterruptedException ex) {
                    throw new RuntimeException(ex);
                }
                pressKey(KeyEvent.VK_TAB);
                robot.keyRelease(KeyEvent.VK_ALT);
                robot.keyRelease(KeyEvent.VK_TAB);
                try {
                    Thread.sleep(100);
                } catch (InterruptedException ex) {
                    throw new RuntimeException(ex);
                }
                // Switching to marking
                robot.keyPress(KeyEvent.VK_ALT);
                robot.keyPress(KeyEvent.VK_J);
                robot.keyRelease(KeyEvent.VK_ALT);
                robot.keyRelease(KeyEvent.VK_J);
                robot.keyPress(KeyEvent.VK_M);
                robot.keyRelease(KeyEvent.VK_M);
                try {
                    Thread.sleep(500);
                } catch (InterruptedException ex) {
                    throw new RuntimeException(ex);
                }
                pressKey(KeyEvent.VK_ENTER);
                try {
                    Thread.sleep(5000);
                } catch (InterruptedException ex) {
                    throw new RuntimeException(ex);
                }
                // Focusing the laser
                pressKeyMultipleTimes(KeyEvent.VK_P, 2);
                try {
                    Thread.sleep(100);
                } catch (InterruptedException ex) {
                    throw new RuntimeException(ex);
                }
                // Return to app so user can notify when done
                robot.keyPress(KeyEvent.VK_ALT);
                try {
                    Thread.sleep(50);
                } catch (InterruptedException ex) {
                    throw new RuntimeException(ex);
                }
                pressKey(KeyEvent.VK_TAB);
                robot.keyRelease(KeyEvent.VK_ALT);
                robot.keyRelease(KeyEvent.VK_TAB);
                try {
                    Thread.sleep(100);
                } catch (InterruptedException ex) {
                    throw new RuntimeException(ex);
                }

            }
        });

        // Add an ActionListener to the Next button
        nextButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                // When the laser is focused and user is ready to engrave
                // Switch back to laser tab
                robot.keyPress(KeyEvent.VK_ALT);
                try {
                    Thread.sleep(50);
                } catch (InterruptedException ex) {
                    throw new RuntimeException(ex);
                }
                pressKey(KeyEvent.VK_TAB);
                robot.keyRelease(KeyEvent.VK_ALT);
                robot.keyRelease(KeyEvent.VK_TAB);
                // Turn off laser
                try {
                    Thread.sleep(1000);
                } catch (InterruptedException ex) {
                    throw new RuntimeException(ex);
                }
                robot.keyPress(KeyEvent.VK_ALT);
                robot.keyPress(KeyEvent.VK_J);
                robot.keyRelease(KeyEvent.VK_ALT);
                robot.keyRelease(KeyEvent.VK_J);
                robot.keyPress(KeyEvent.VK_M);
                robot.keyRelease(KeyEvent.VK_M);
                try {
                    Thread.sleep(500);
                } catch (InterruptedException ex) {
                    throw new RuntimeException(ex);
                }
                pressKeyMultipleTimes(KeyEvent.VK_P, 2);
                // Switch back to app
                robot.keyPress(KeyEvent.VK_ALT);
                try {
                    Thread.sleep(50);
                } catch (InterruptedException ex) {
                    throw new RuntimeException(ex);
                }
                pressKey(KeyEvent.VK_TAB);
                robot.keyRelease(KeyEvent.VK_ALT);
                robot.keyRelease(KeyEvent.VK_TAB);

                engraveBatchPanel();
            }
        });

        getContentPane().removeAll();
        // Add components to the fixturePanel
        GridBagConstraints gbc = new GridBagConstraints();
        gbc.gridx = 0;
        gbc.gridy = 0;
        gbc.insets = new Insets(10, 10, 10, 10);
        add(batchLabel, gbc);
        gbc.gridy = 1;
        add(focusLabel, gbc);
        gbc.gridy = 2;
        add(focusButton, gbc);
        gbc.gridy = 3;
        add(laserCheck, gbc);
        gbc.gridy = 4;
        add(nextButton, gbc);
        revalidate();
        repaint();

    }

    private void engraveBatchPanel(){
        JLabel checkLaser = new JLabel("Close the Cover");
        JCheckBox laserCheck = new JCheckBox("Cover is closed and laser is ready to engrave.");
        JButton engraveButton = new JButton("Fire");

        engraveButton.setEnabled(false);    // Disable the Next button initially
        // Add an ItemListener to the checkbox
        laserCheck.addItemListener(new ItemListener() {
            @Override
            public void itemStateChanged(ItemEvent e) {
                engraveButton.setEnabled(e.getStateChange() == ItemEvent.SELECTED); // Enable or disable the Next button based on the checkbox state
            }
        });

        // Add an ActionListener to the Next button
        engraveButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                // CREATE DC_SN for the batch when user presses "Fire"
                DCSN_Generator();   // TODO: generate DCSN at the end of batch? What if they shut the program down mid-batch?
                // Inserting products into Database TODO: Make this into a seperate function
                String connectionUrl =
                        "jdbc:sqlserver://BTI-PC37\\SQLEXPRESS;"
                                + "port=49170;"
                                + "database=AppleCore;"
                                + "user=ApolloBow1;"
                                + "password=8goodfood!;"
                                + "encrypt=true;"
                                + "trustServerCertificate=true;"
                                + "loginTimeout=1;";

                try (Connection connection = DriverManager.getConnection(connectionUrl)){
                    Statement statement = connection.createStatement();

                    for (Product product : productList) {
                        String sql = "INSERT INTO DC_SN(Crystal_DC_SN) VALUES ('" + product.getDateCodeSerialNumber() + "')";
                        System.out.println(sql);        // Print DCSNs to the terminal
                        statement.executeUpdate(sql);   // Execute SQL statement
                    }
                } catch (SQLException ex) {
                    ex.printStackTrace();
                    // Handle SQL exception
                }

                // Subtract the engraved parts from the partsLeft column
                String updateQuery = "UPDATE ETCHER_TRACKER SET partsLeft = partsLeft - ? WHERE workOrder = ?";
                try {
                    PreparedStatement updateStatement = connectionA.prepareStatement(updateQuery);
                    updateStatement.setInt(1, productList.size()); // Number of parts engraved in the current batch
                    updateStatement.setString(2, workOrderInput);
                    updateStatement.executeUpdate();
                    updateStatement.close();
                } catch (SQLException ex) {
                    ex.printStackTrace();
                    // Handle SQL exception
                }

                productList.clear();    // Clear the List for the next batch

                // Switch back to Laser Software
                switchTabs();
                try {
                    Thread.sleep(1000);
                } catch (InterruptedException ex) {
                    throw new RuntimeException(ex);
                }
                altJM();    // Alt + J + M
                try {
                    Thread.sleep(50);
                } catch (InterruptedException ex) {
                    throw new RuntimeException(ex);
                }
                pressKey(KeyEvent.VK_L);
                pressKey(KeyEvent.VK_M);
                try {
                    Thread.sleep(500);
                } catch (InterruptedException ex) {
                    throw new RuntimeException(ex);
                }
                // Pressing the "Trigger" button for the engraver
                altJM();
                try {
                    Thread.sleep(50);
                } catch (InterruptedException ex) {
                    throw new RuntimeException(ex);
                }
                robot.keyPress(KeyEvent.VK_ALT);
                robot.keyPress(KeyEvent.VK_T);
                robot.keyRelease(KeyEvent.VK_ALT);
                robot.keyRelease(KeyEvent.VK_T);
                robot.keyPress(KeyEvent.VK_G);
                robot.keyRelease(KeyEvent.VK_G);
                try {
                    Thread.sleep(500);
                } catch (InterruptedException ex) {
                    throw new RuntimeException(ex);
                }
                // Switch back to Java App
                switchTabs();
                createWaitingPanel();
            }
        });

        getContentPane().removeAll();
        // Add components to the fixturePanel
        GridBagConstraints gbc = new GridBagConstraints();
        gbc.gridx = 0;
        gbc.gridy = 0;
        gbc.insets = new Insets(10, 10, 10, 10);
        add(checkLaser, gbc);
        gbc.gridy = 1;
        add(laserCheck, gbc);
        gbc.gridy = 2;
        add(engraveButton, gbc);
        revalidate();
        repaint();

    }

    private void createWaitingPanel(){
        JLabel waitingLabel = new JLabel("Laser is engraving Batch: " + currentBatch + " of " + totalBatches + "... Prepare next batch.");
        JButton nextButton = new JButton("Next");

        nextButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                if (currentBatch < totalBatches) {
                    currentBatch++; // increase batch size by 1
                    grabFixturePanel();

                } else {
                    JOptionPane.showMessageDialog(null, "All batches processed. Program will now exit.");
                    try {
                        connectionX.close();    // Close the Xtuple connection
                    } catch (SQLException ex) {
                        throw new RuntimeException(ex);
                    }
                    System.exit(0);
                }
            }
        });

        getContentPane().removeAll();
        // Add components to the fixturePanel
        GridBagConstraints gbc = new GridBagConstraints();
        gbc.gridx = 0;
        gbc.gridy = 0;
        gbc.insets = new Insets(10, 10, 10, 10);
        add(waitingLabel, gbc);
        gbc.gridy = 1;
        add(nextButton);
        revalidate();
        repaint();

    }

    private void retrieveWorkOrderInformation(String workOrderInput){
        String query = "SELECT * FROM wo WHERE wo_number::varchar = ?";

        try {
            PreparedStatement statement = connectionX.prepareStatement(query);
            statement.setString(1, workOrderInput);
            ResultSet resultSet = statement.executeQuery();

            if (resultSet.next()) {
                itemQuantity = resultSet.getInt("wo_qtyrcv");   // column for quantity is: wo_qtyrcv. TODO: Make it so that the qty = row[9]
                System.out.println(itemQuantity);
                if(checkWorkOrderExistence(workOrderInput)){
                    // Work order already exists, update partsLeft and totalParts
                    String updateQuery = "UPDATE ETCHER_TRACKER SET partsLeft = ?, totalParts = ? WHERE workOrder = ?";
                    PreparedStatement updateStatement = connectionA.prepareStatement(updateQuery);
                    updateStatement.setInt(1, itemQuantity);
                    updateStatement.setInt(2, itemQuantity);
                    updateStatement.setString(3, workOrderInput);
                    updateStatement.executeUpdate();
                    updateStatement.close();
                }
                else {
                    // Work order is new, insert a new row
                    String insertQuery = "INSERT INTO ETCHER_TRACKER (workOrder, partsLeft, totalParts) VALUES (?, ?, ?)";
                    PreparedStatement insertStatement = connectionA.prepareStatement(insertQuery);
                    insertStatement.setString(1, workOrderInput);
                    insertStatement.setInt(2, itemQuantity);
                    insertStatement.setInt(3, itemQuantity);
                    insertStatement.executeUpdate();
                    insertStatement.close();
                    connectionA.commit();
                }
                existsInDatabase = true;
            } else {
                existsInDatabase = false;
                JOptionPane.showMessageDialog(null, "Work order not found.");
            }

            resultSet.close();
            statement.close();
        } catch (SQLException e) {
            e.printStackTrace();
            JOptionPane.showMessageDialog(null, "Error retrieving work order information.");
        }

    }

    private void connectXtupleReal(){
        try {
            String url = "jdbc:postgresql://bliley_prod.xtuplecloud.com:5432/bliley_605_live?user=admin&password=BTech1";
            connectionX = DriverManager.getConnection(url);

        } catch (Exception e) {
            e.printStackTrace();
            JOptionPane.showMessageDialog(null, "Error connecting to the Xtuple database.");
        }
    }

    private void connectAppleCore(){
        String connectionUrl =
                "jdbc:sqlserver://BTI-PC37\\SQLEXPRESS;"
                        + "port=49170;"
                        + "database=AppleCore;"
                        + "user=ApolloBow1;"
                        + "password=8goodfood!;"
                        + "encrypt=true;"
                        + "trustServerCertificate=true;"
                        + "loginTimeout=1;";

        try {
            connectionA = DriverManager.getConnection(connectionUrl);

        } catch (SQLException ex) {
            ex.printStackTrace();
            JOptionPane.showMessageDialog(null, "Error connecting to the AppleCore database.");
        }
    }

    // check if work order exists in the ETCHER_TRACKER table
    private boolean checkWorkOrderExistence(String workOrder) {
        String query = "SELECT COUNT(*) FROM ETCHER_TRACKER WHERE workOrder = ?";
        try {
            PreparedStatement statement = connectionA.prepareStatement(query);
            statement.setString(1, workOrder);
            ResultSet resultSet = statement.executeQuery();
            resultSet.next();
            int count = resultSet.getInt(1);
            resultSet.close();
            statement.close();
            return count > 0;
        } catch (SQLException e) {
            e.printStackTrace();
            JOptionPane.showMessageDialog(null, "Error checking work order existence.");
            return false;
        }
    }

    // Grabs the amount of parts left
    private int getPartsLeft(String workOrder) {
        String query = "SELECT partsLeft FROM ETCHER_TRACKER WHERE workOrder = ?";                                      //
        try {
            PreparedStatement statement = connectionA.prepareStatement(query);                                          //
            statement.setString(1, workOrder);
            ResultSet resultSet = statement.executeQuery();
            if (resultSet.next()) {
                int partsLeft = resultSet.getInt("partsLeft");
                resultSet.close();
                statement.close();
                return partsLeft;
            }
            resultSet.close();
            statement.close();
        } catch (SQLException e) {
            e.printStackTrace();
            // Handle SQL exception
        }
        return 0; // Return 0 if the work order doesn't exist or there is an error
    }

    public int getLatestDC( ){
        String latestDC = "";
        try {
            String connectionUrl =
                    "jdbc:sqlserver://BTI-PC37\\SQLEXPRESS;"
                            + "port=49170;"
                            + "database=AppleCore;"
                            + "user=ApolloBow1;"
                            + "password=8goodfood!;"
                            + "encrypt=true;"
                            + "trustServerCertificate=true;"
                            + "loginTimeout=1;";

            Connection connection = DriverManager.getConnection(connectionUrl);

            // Execute a SQL query to retrieve the maximum serial number from the database
            String query = "SELECT MAX(Crystal_DC_SN) FROM DC_SN";
            Statement statement = connection.createStatement();
            ResultSet resultSet = statement.executeQuery(query);

            if (resultSet.next()) {
                latestDC = resultSet.getString(1);
            }

            resultSet.close();
            statement.close();
            connection.close();

            if (latestDC == null) {
                return 0;
            }

            String[] splitter = (latestDC.split("\\.",2));  // Splits the DATE CODE and Serial Number
            if(splitter[0].substring(0,2).equals(currentYear) && splitter[0].substring(2,4).equals(currentWeek)){
                return Integer.parseInt(splitter[1]);
            }

        } catch (SQLException e) {
            e.printStackTrace();
            // Handle the exception appropriately
        }

        return 0;
    }

    public void DCSN_Generator() {
        LocalDate currentDate = LocalDate.now();
        int year = currentDate.getYear();
        int week = currentDate.get(WeekFields.ISO.weekOfWeekBasedYear());
        int lastSerialNumber = getLatestDC();   // Retrieve the last used serial number from the database
        int serialNumber = (lastSerialNumber + 1);  // Increment the last serial number to start the next sequence

        int itemsInLastBatch = itemQuantity % fixtureCapacity;  // The last batch is the remainder of the (itemQuantity) / (fixtureCapacity)
        int currentBatchToBeEngraved;   // The batch that is being engraved
        if(currentBatch != totalBatches){   // if it is not the last batch
            currentBatchToBeEngraved = fixtureCapacity; // The amount of items to be engraved is the # items that a fixture can hold
        } else {
            currentBatchToBeEngraved = itemsInLastBatch;    // The last batch is the remaining items
        }

        for (int r = 0; r < currentBatchToBeEngraved; r++) {
            String formattedSerialNumber = String.format("%05d", serialNumber);
            String gridText = String.format("%02d%02d.%s", year % 100, week, formattedSerialNumber);

            Product product = new Product(gridText);
            productList.add(product);
            serialNumber++;

            // Check if the week has changed
            LocalDate newDate = LocalDate.now();
            int newWeek = newDate.get(WeekFields.ISO.weekOfWeekBasedYear());
            if (newWeek != week) {
                week = newWeek; // Update the week to the new week
                serialNumber = 1; // Reset the serial number to 1
            }

        }
    }

    /**
     * The following section is the Keystroke implementation of the App.
     */
    private void enteringDCSN() {
        String crystalName = "QC10K5LNG0000_QR";    // TODO: Ask Doug or someone to see how to grab the item number from the WO
        String filePath = "C:\\Users\\Laser Marker\\Desktop\\Crystal Cans with QR\\" + crystalName + ".MX4"; // TODO: Update with file path depending on the item number

        File file = new File(filePath);
        File file2 = new File(selectedFilePath);

        if (Desktop.isDesktopSupported() && file.exists()) {
            try {
                    if(currentBatch == 1){                                                                              //! if it is the first batch
                    Desktop.getDesktop().open(file2);                                                                   // User's file that they selected from the Fixture Panel
                    Thread.sleep(25000);                                                                           // Waits 22 seconds for the file to open (Worst Case)
                    robot.keyPress(KeyEvent.VK_WINDOWS);                                                                // MAXIMIZE WINDOW
                    pressKey(KeyEvent.VK_UP);
                    robot.keyRelease(KeyEvent.VK_WINDOWS);
                    Thread.sleep(2000);
                }
                else {
                    switchTabs();
                    Thread.sleep(100);
                    robot.keyPress(KeyEvent.VK_ALT);
                    Thread.sleep(50);
                    pressKey(KeyEvent.VK_H);
                    robot.keyRelease(KeyEvent.VK_ALT);
                    Thread.sleep(2000);
                }
                // Performing the Keystrokes
                robot.mouseMove(0,0);
                Thread.sleep(1000);
                robot.mouseMove(1900,310);  // Positioning for the Bar code
                //! moving mouse to the Bar code
                Thread.sleep(1500); // wait 1.5 seconds
                robot.mousePress(InputEvent.BUTTON1_DOWN_MASK);                                                         // 1/2 Single clicks to make it a Double Click
                robot.mouseRelease(InputEvent.BUTTON1_DOWN_MASK);
                robot.mousePress(InputEvent.BUTTON1_DOWN_MASK);                                                         // 2/2 Single clicks to make it a Double Click
                robot.mouseRelease(InputEvent.BUTTON1_DOWN_MASK);
                System.out.println("First double click");
                Thread.sleep(2000);                                                                                // wait 2 seconds after clicking
                robot.mouseMove(600,652);                                                                          // moving mouse to enter DC SN
                Thread.sleep(1500);                                                                                // wait 1.5 seconds after clicking
                robot.mousePress(InputEvent.BUTTON1_DOWN_MASK);                                                         // 2 Single clicks to make it a Double Click
                robot.mouseRelease(InputEvent.BUTTON1_DOWN_MASK);
                robot.mousePress(InputEvent.BUTTON1_DOWN_MASK);
                robot.mouseRelease(InputEvent.BUTTON1_DOWN_MASK);
                Thread.sleep(3000);                                                                                // wait 3 seconds after clicking
                System.out.println("Second double click");
                pressKeyMultipleTimes(KeyEvent.VK_TAB, 6);
                Thread.sleep(1000);
                pressKey(KeyEvent.VK_ENTER);
                Thread.sleep(1000);
                pressKeyMultipleTimes(KeyEvent.VK_TAB, 2);
                Thread.sleep(1000);
                // ENTERING SERIAL NUMBER INTO THE COUNTER
                pSerialNumber = getLatestDC() + 1;  // printSerialNumber
                String serialNumberString = String.valueOf(pSerialNumber);
                for (int i = 0; i < serialNumberString.length(); i++) {
                    char c = serialNumberString.charAt(i);
                    pressKey(Character.toUpperCase(c));
                }
                Thread.sleep(1000);
                System.out.println("String Entered Correctly");
                pressKeyMultipleTimes(KeyEvent.VK_TAB, 8);
                Thread.sleep(1000);
                pressKey(KeyEvent.VK_ENTER);
                Thread.sleep(500);
                pressKey(KeyEvent.VK_ENTER);
                Thread.sleep(4000);
                pressKeyMultipleTimes(KeyEvent.VK_TAB, 5);
                Thread.sleep(1000);
                pressKey(KeyEvent.VK_ENTER);
                System.out.println("Tab pressed 5 times, then enter ");
                Thread.sleep(1000);
                // For pressing Shift + Tab 6 times
                robot.keyPress(KeyEvent.VK_SHIFT);
                Thread.sleep(500);
                for (int i = 0; i < 6; i++) {
                    robot.keyPress(KeyEvent.VK_TAB);
                    Thread.sleep(20);
                    robot.keyRelease(KeyEvent.VK_TAB);
                    Thread.sleep(20);
                }
                robot.keyRelease(KeyEvent.VK_SHIFT);
                System.out.println("Shift + Tab entered 6 times");
                Thread.sleep(1000);
                pressKey(KeyEvent.VK_ENTER);
                Thread.sleep(1000);
                pressKeyMultipleTimes(KeyEvent.VK_TAB, 20);
                Thread.sleep(500);
                pressKey(KeyEvent.VK_ENTER);
                Thread.sleep(500);
                pressKey(KeyEvent.VK_ESCAPE);
                System.out.println("escape entered");

                placeFixturePanel();
                requestFocus();

            } catch (IOException | InterruptedException e) {
                e.printStackTrace();
            }
        } else {
            System.err.println("Failed to open the file.");
        }
    }

    private void pressKey(int keyCode) {
        robot.keyPress(keyCode);
        robot.keyRelease(keyCode);
    }

    private void pressKeyMultipleTimes(int keyCode, int times) {
        for (int i = 0; i < times; i++) {
            pressKey(keyCode);
        }
    }

    private int calculateTotalBatches(int partsLeft, int fixtureCapacity) {
        int batches = partsLeft / fixtureCapacity;
        if (partsLeft % fixtureCapacity != 0) {
            batches++;
        }
        return batches;
    }

    private void switchTabs(){
        robot.keyPress(KeyEvent.VK_ALT);
        try {
            Thread.sleep(50);
        } catch (InterruptedException ex) {
            throw new RuntimeException(ex);
        }
        pressKey(KeyEvent.VK_TAB);
        robot.keyRelease(KeyEvent.VK_ALT);
        robot.keyRelease(KeyEvent.VK_TAB);
    }

    private void altJM(){
        robot.keyPress(KeyEvent.VK_ALT);
        robot.keyPress(KeyEvent.VK_J);
        robot.keyRelease(KeyEvent.VK_ALT);
        robot.keyRelease(KeyEvent.VK_J);
        robot.keyPress(KeyEvent.VK_M);
        robot.keyRelease(KeyEvent.VK_M);
    }

    private static void setDefaultFontSize() {
        // Get the current default font
        FontUIResource font = new FontUIResource(UIManager.getFont("Label.font"));

        // Create a new font with the desired size
        FontUIResource newFont = new FontUIResource(font.getFontName(), font.getStyle(), 20);

        // Set the new default font for all Swing components
        Enumeration<Object> keys = UIManager.getDefaults().keys();
        while (keys.hasMoreElements()) {
            Object key = keys.nextElement();
            Object value = UIManager.get(key);
            if (value instanceof FontUIResource) {
                UIManager.put(key, newFont);
            }
        }
    }

    public static void main(String[] args) {
        setDefaultFontSize();

        SwingUtilities.invokeLater(() -> {
            LaserMarker laserMarker = new LaserMarker();
            laserMarker.setSize(1680, 1080); // Set the size of the frame
            laserMarker.setExtendedState(JFrame.MAXIMIZED_BOTH);
        });
    }

}

